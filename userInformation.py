


from tkinter import messagebox

import face
import userPass


def GetUserInfo(search_topic_recieved, numberofpost):
    if search_topic_recieved:
        if search_topic_recieved != "תכניס נושא חיפוש":
            # try:
            if int(numberofpost) != 0:
                if messagebox.askokcancel('Application','Application is running, press OK to continue') == True:
                    username = userPass.getUser()
                    password = userPass.getPass()
                    # try:
                    print(search_topic_recieved)
                    FB = face.store_post_information(username, password)
                    FB.login()
                    FB.store_post(search_topic_recieved)

                    # except:
                    #     messagebox.showerror("Could not execute task. Please try again.")

                else:
                    SystemExit()
            else:
                messagebox.showwarning("Error", "Please enter a valid number of posts to like")
                print("Please enter a valid number of posts")
            # except Exception:
            #     messagebox.showwarning("Error", "Please enter a valid number of posts to like")
            #     print("Please enter a valid number of posts to like")
        else:
            messagebox.showwarning("Error", "Please enter suitable data")
            print("Please enter suitable data")
    else:
        messagebox.showwarning('Error', 'Please enter a username or password')  #shows warning message
        print("Please enter a username and password")
