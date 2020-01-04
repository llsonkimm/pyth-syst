import sqlite3
import tkinter.messagebox as tkMessageBox
from tkinter import *

root = Tk()
root.title("Python: Employee Registration")
# photo = PhotoImage(file="images.gif")
# w = Label(compound=CENTER,image=photo).pack(side="top")
width = 900
height = 700
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

FIRST_NAME = StringVar()
MIDDLE_NAME = StringVar()
LAST_NAME = StringVar()
ID_NUMBER = StringVar()
AGE = StringVar()
DATE_OF_BIRTH = StringVar()
PHONE_NUMBER = StringVar()
EMAIL_ADDRESS = StringVar()
RESIDENCE = StringVar()
GENDER = StringVar()


def Database():
    global conn, cursor
    conn = sqlite3.connect("Employees.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `members` (member_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, firstname TEXT, "
        "middlename TEXT, lastname TEXT,  gender TEXT, age INTEGER, idnumber INTEGER, dateofbirth TEXT, phonenumber "
        "INTEGER, "
        "emailaddress TEXT, residence TEXT)")


def Exit():
    result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


def RegisterForm():
    global RegisterFrame, lbl_result2
    RegisterFrame = Frame(root)
    RegisterFrame.pack(side=TOP, pady=10)
    Tk.RegisterFrame = PhotoImage(file="images.gif")
    lbl_register = Label(RegisterFrame, text="PROCEED TO REGISTER NEW EMPLOYEE", fg="Blue",
                         font=('times', 13))
    lbl_register.grid(row=0)
    lbl_first_name = Label(RegisterFrame, text="Enter First Name as appears on the ID:", font=('times', 13), bd=15)
    lbl_first_name.grid(row=1)
    lbl_middle_name = Label(RegisterFrame, text="Enter Middle Name as appears on the ID:", font=('times', 13), bd=15)
    lbl_middle_name.grid(row=2)
    lbl_last_name = Label(RegisterFrame, text="Enter Last Name as appears on the ID:", font=('times', 13), bd=15)
    lbl_last_name.grid(row=3)
    lbl_gender = Label(RegisterFrame, text="Choose Sex of the Employee:", font=('times', 13), bd=15)
    lbl_gender.grid(row=4)
    lbl_id_number = Label(RegisterFrame, text="Enter ID Number:", padx=5, font=('times', 13), bd=15)
    lbl_id_number.grid(row=5)
    lbl_age = Label(RegisterFrame, text="Enter Age of the Employee:", font=('times', 13), bd=15)
    lbl_age.grid(row=6)
    lbl_date_of_birth = Label(RegisterFrame, text="Enter Date of Birth as appears on the ID:", font=('times', 13),
                              bd=15)
    lbl_date_of_birth.grid(row=7)
    lbl_phone_number = Label(RegisterFrame, text="Enter Phone Number:", font=('times', 13), bd=15)
    lbl_phone_number.grid(row=8)
    lbl_email_address = Label(RegisterFrame, text="Enter Email Address:", font=('times', 13), bd=15)
    lbl_email_address.grid(row=9)
    lbl_residence = Label(RegisterFrame, text="Enter Place of Residence:", font=('times', 13), bd=15)
    lbl_residence.grid(row=10)
    lbl_result2 = Label(RegisterFrame, text="", font=('times', 18))
    lbl_result2.grid(row=11, columnspan=2)
    first_name = Entry(RegisterFrame, font=('times', 13), textvariable=FIRST_NAME, width=15)
    first_name.grid(row=1, column=1)
    middle_name = Entry(RegisterFrame, font=('times', 13), textvariable=MIDDLE_NAME, width=15)
    middle_name.grid(row=2, column=1)
    last_name = Entry(RegisterFrame, font=('times', 13), textvariable=LAST_NAME, width=15)
    last_name.grid(row=3, column=1)
    id_number = Entry(RegisterFrame, font=('times', 13), textvariable=ID_NUMBER, width=15)
    id_number.grid(row=5, column=1)
    age = Entry(RegisterFrame, font=('times', 13), textvariable=AGE, width=15)
    age.grid(row=6, column=1)
    date_of_birth = Entry(RegisterFrame, font=('times', 13), textvariable=DATE_OF_BIRTH, width=15)
    date_of_birth.grid(row=7, column=1)
    phone_number = Entry(RegisterFrame, font=('times', 13), textvariable=PHONE_NUMBER, width=15)
    phone_number.grid(row=8, column=1)
    email_address = Entry(RegisterFrame, font=('times', 13), textvariable=EMAIL_ADDRESS, width=15)
    email_address.grid(row=9, column=1)
    residence = Entry(RegisterFrame, font=('times', 13), textvariable=RESIDENCE, width=15)
    residence.grid(row=10, column=1)
    var = IntVar()
    Radiobutton(root, text="M", padx=5, variable=var, value=1, font=('times', 13)).place(x=580, y=203)
    Radiobutton(root, text="F", padx=20, variable=var, value=2, font=('times', 13)).place(x=630, y=203)
    btn_register = Button(RegisterFrame, text="Register", font=('times', 18), bg='brown', fg='white', width=35)
    btn_register.grid(row=11, columnspan=2, pady=20)
    btn_register.bind('<Button-1>', Register())




def Register():
    Database()
    if FIRST_NAME.get() == "" or LAST_NAME.get() == "" or EMAIL_ADDRESS.get() == "" or RESIDENCE.get() == "" or \
            ID_NUMBER.get() == "" or DATE_OF_BIRTH.get() == "" or GENDER.get() == "" or PHONE_NUMBER.get() == "":
        lbl_result2.config(text="Please complete the required field!", fg="orange")
    else:
        cursor.execute("SELECT * FROM `members` WHERE `idnumber` = ? and 'phonenumber' = ")
        if cursor.fetchone() is not None:
            lbl_result2.config(text="ID Number is already taken", fg="red")
        else:
            cursor.execute("INSERT INTO `members` (firstname, middlename, lastname, idnumber, age, dateofbirth, gender,"
                           "phonenumber, emailadress, residence) VALUES(?, ?, ?, ?,?,?,?,?,?,?)",
                           (str(FIRST_NAME.get()), str(MIDDLE_NAME.get()), str(LAST_NAME.get()), str(ID_NUMBER.get()),
                            str(AGE.get()), str(DATE_OF_BIRTH.get()), str(GENDER.get()), str(PHONE_NUMBER.get()),
                            str(EMAIL_ADDRESS.get()), str(RESIDENCE.get())))
            conn.commit()
            FIRST_NAME.set("")
            MIDDLE_NAME.set("")
            LAST_NAME.set("")
            ID_NUMBER.set("")
            AGE.set("")
            DATE_OF_BIRTH.set("")
            GENDER.set("")
            PHONE_NUMBER.set("")
            EMAIL_ADDRESS.set("")
            RESIDENCE.set("")
            lbl_result2.config(text="Successfully Created!", fg="black")
    cursor.close()
    conn.close()


RegisterForm()

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=Exit)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

# INITIALIZATION
if __name__ == '__main__':
    root.mainloop()
