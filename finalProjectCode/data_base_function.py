import sqlite3


#not database
def valid(topic):#validation of search word
    if(topic=="" or topic=="$"): #or topic=="תכניס נושא לחיפוש"  sometimes there are post for this topic
        return 1
    return 0

def find_min(list_search):#a function to find the minimum out of a list of classes bcs the smallest strings returns the date of post

    x = "l94mrbxd.aenfhxwr.myohyog2.b6zbclly.l9j0dhe7.sdhka5h4.nw7X6Rf if you see this autput probably its a new acount"
    for i in list_search:
        if (len(i) < len(x)):#the min string frome the list
            x = i
            if (x.endswith('h4') == True):#this is for if thre are few posts at the same page so it will bring  the first
                return x
    if(x.endswith('h4')==True):#if it is the date path return because usually it shorter then the others
        return x
    else:
        for right in list_search:#if the date path is longer than the others
            if(right.endswith('h4')==True):
                return right
    return x


#database

def all_saved_topics(currUser):
    conn = sqlite3.connect('images/projectManagment.db')
    cursor = conn.execute(
        f"SELECT topic,UserName FROM topics  WHERE UserName='{currUser}' ORDER BY id DESC limit 10");  # take the last 10
    list_res = cursor.fetchall()

    conn.close()
    return list_res


def del_all_topics(currUser):
    # Create a database or connect to one
    conn = sqlite3.connect('images/projectManagment.db')
    # Create cursor
    c = conn.cursor()

    # Delete a record
    c.execute(f"DELETE from topics WHERE UserName='{currUser}'");  # check if it did this

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()


def del_topic(topic,user):
    # Create a database or connect to one
    conn = sqlite3.connect('images/projectManagment.db')
    # Create cursor
    c = conn.cursor()

    # Delete a record
    c.execute(f"DELETE from topics WHERE topic = '{topic}' AND UserName='{user}'");  # check if it did this

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()


def update_post_comment(comment,link,user):#
    # Create a database or connect to one
    conn = sqlite3.connect('images/projectManagment.db')
    # Create cursor
    c = conn.cursor()

    # update query to update comment
    c.execute(
        f"UPDATE posts set comment = '{comment}' where link = '{link}' AND UserName='{user}'");  # check if it did this

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()




def dele_post(link,user):
    # Create a database or connect to one
    conn = sqlite3.connect('images/projectManagment.db')
    # Create cursor
    c = conn.cursor()

    # Delete a record
    c.execute(
        f"DELETE from posts WHERE link = '{link}' AND UserName='{user}'");  # check if it did this AND user=user add----------------------

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()


def del_all_posts(if_topic,s,currUser):
    conn = sqlite3.connect('images/projectManagment.db')
    if (if_topic == "$"):  # delete all
        conn.execute(f"DELETE  FROM posts  WHERE UserName='{currUser}'");
    else:  # delete for topic
        conn.execute(f"DELETE  FROM posts  WHERE UserName='{currUser}' AND subject LIKE '{s}'");
    conn.commit()
    conn.close()


def store_posts_for(currUser,s):
    conn = sqlite3.connect('images/projectManagment.db')
    cursor = conn.execute(f"SELECT * FROM posts  WHERE UserName='{currUser}' AND subject LIKE '{s}'");
    list=cursor.fetchall()

    conn.close()
    return list

def store_all_posts(currUser):
    conn = sqlite3.connect('images/projectManagment.db')
    cursor = conn.execute(f"SELECT * FROM posts  WHERE UserName='{currUser}'");
    list=cursor.fetchall()
    conn.close()
    return list

def add_topic_try(search_topic,currUser):
    conn = sqlite3.connect('images/projectManagment.db')
    curser = conn.execute(
        f"SELECT topic,UserName FROM topics  WHERE topic='{search_topic}' AND UserName='{currUser}'");
    help = curser.fetchall()[0]
    a = help[1]
    conn.execute(f"DELETE FROM topics  WHERE topic='{search_topic}' AND UserName='{currUser}'");
    conn.execute("INSERT INTO topics  VALUES (?,?,?)", (None, search_topic, currUser));
    conn.commit()
    print("try to save the same word to same user comment for me")
    conn.close()



def add_topic(search_topic,currUser):
    conn = sqlite3.connect('images/projectManagment.db')
    conn.execute("INSERT INTO topics  VALUES (?,?,?)", (None, search_topic, currUser));
    conn.commit()
    conn.close()

def try_exist_post(link,currUser):
    conn = sqlite3.connect('images/projectManagment.db')
    cursor = conn.execute(
        f"SELECT link,UserName FROM posts  WHERE link='{link}' AND UserName='{currUser}'");  # if the post saved
    help = cursor.fetchall()[0]
    a = help[1]
    conn.close()

def insert_post_again(k,posts_details,search_topic,currUser,comment_text):
    conn = sqlite3.connect('images/projectManagment.db')
    conn.execute(f"DELETE from posts WHERE link = '{posts_details[0][k - 2]}' AND UserName='{currUser}'");

    conn.execute(
        "INSERT INTO posts (id,link,writer,date,content,comment,subject,username) VALUES (?,?,?,?,?,?,?,?)", (
            None, posts_details[0][k - 2], posts_details[1][k - 2], posts_details[2][k - 2],
            posts_details[3][k - 2],
            comment_text, search_topic, currUser));
    conn.commit()
    conn.close()

def insert_post(k,posts_details,search_topic,currUser,comment_text):
    conn = sqlite3.connect('images/projectManagment.db')
    conn.execute("INSERT INTO posts (id,link,writer,date,content,comment,subject,username) VALUES (?,?,?,?,?,?,?,?)", (
        None, posts_details[0][k - 2], posts_details[1][k - 2], posts_details[2][k - 2], posts_details[3][k - 2],
        comment_text, search_topic, currUser));
    conn.commit()
    conn.close()



def insert_user_try(username,password):
    conn = sqlite3.connect('images/projectManagment.db')
    conn.execute("INSERT INTO users (UserName,Password,Name) VALUES (?,?,?)", (username, password, "try"));
    conn.commit()

    conn.execute(f"DELETE from users WHERE UserName = '{username}'");
    conn.commit()

    conn.close()


def insert_user(username, password, name):
    conn = sqlite3.connect('images/projectManagment.db')
    conn.execute("INSERT INTO users (UserName,Password,Name) VALUES (?,?,?)", (username, password, name));
    conn.commit()
    conn.close()

def del_user(userToDeleteOrUpdate):
    conn = sqlite3.connect('images/projectManagment.db')
    conn.execute("PRAGMA foreign_keys = 1")
    cur = conn.cursor()
    cursur = cur.execute(
        f"SELECT * FROM users  WHERE UserName='{userToDeleteOrUpdate}'");  # for checking bcs the delete doesnt returns error if not exist
    cursur.fetchone()[0]
    cur.execute(f"DELETE from users WHERE UserName = '{userToDeleteOrUpdate}'");

    conn.commit()
    conn.close()

def update_pass_user(userToDeleteOrUpdate,passw):
    conn = sqlite3.connect('images/projectManagment.db')
    conn.execute("PRAGMA foreign_keys = 1")
    cur = conn.cursor()
    cursur = cur.execute(
        f"SELECT * FROM users  WHERE UserName='{userToDeleteOrUpdate}'");  # for checking bcs the delete doesnt returns error if not exist
    cursur.fetchone()[0]
    cur.execute(f"UPDATE users SET Password='{passw}' WHERE UserName = '{userToDeleteOrUpdate}'");

    conn.commit()
    conn.close()

def select_users():#for testing
    conn = sqlite3.connect('images/projectManagment.db')
    cur = conn.cursor()
    cursor = cur.execute("SELECT * from users")
    list=cursor.fetchall()
    conn.close()
    return list


