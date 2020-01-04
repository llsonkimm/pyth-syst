import sqlite3
import tkinter.messagebox as tkMessageBox
from tkinter import *

root = Tk()
root.title("Python: Administrative Console")
width = 640
height = 480
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

USERNAME = StringVar()
PASSWORD = StringVar()


def Database():
    global conn, cursor
    conn = sqlite3.connect("Administrator.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, "
        "password TEXT)")


def Exit():
    result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


def LoginForm():
    global LoginFrame, lbl_result1
    LoginFrame = Frame(root)
    LoginFrame.pack(side=TOP, pady=80)
    lbl_username = Label(LoginFrame, text="Username:", font=('times', 25), bd=15)
    lbl_username.grid(row=1)
    lbl_password = Label(LoginFrame, text="Password:", font=('times', 25), bd=15)
    lbl_password.grid(row=2)
    lbl_result1 = Label(LoginFrame, text="", font=('times', 18))
    lbl_result1.grid(row=3, columnspan=2)
    username = Entry(LoginFrame, font=('times', 15), textvariable=USERNAME, width=23)
    username.grid(row=1, column=1)
    password = Entry(LoginFrame, font=('times', 15), textvariable=PASSWORD, width=23, show="*")
    password.grid(row=2, column=1)
    btn_login = Button(LoginFrame, text="Login", font=('arial', 18), width=35, command=Login)
    btn_login.grid(row=5, columnspan=2, pady=20)


def Login():
    Database()
    if not (not (USERNAME.get == "") and not (PASSWORD.get() == "")):
        lbl_result1.config(text="Please complete the required field!", fg="orange")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = 'lson' and `password` = 'forgive'")
        conn.commit()
        if cursor.fetchone() is not None:
            import member
        else:
            lbl_result1.config(text="Invalid Username or password", fg="red")


LoginForm()

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=Exit)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

# ========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()
