from tkinter import *
import sqlite3
import os
from tkinter.font import Font

db = sqlite3.connect(f'user_details_database.db')
cursor = db.cursor()

def home():

    root = Tk()
    root.state("zoomed")
    root.configure(background="#ECE5DD")

    fontFamily = StringVar(value="Verdana")
    fontSize = IntVar(value=20)

    appfont = Font(family=fontFamily.get(), size=fontSize.get(), weight='bold')

    Label(root,text="WELCOME TO BHANJA BANK!", bg="#ECE5DD", font=appfont).place(relx=0.35,rely=0.025)

    Label(root,text="GOOD TO SEE YOU HERE !", bg="#ECE5DD")
    root.mainloop()

def create_table():
    sql = f'''
             CREATE TABLE users (
                 ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 name           VARCHAR(256) NOT NULL,
                 email               VARCHAR(256) NOT NULL,
                 current_balance     INTEGER NOT NULL,
                 address     VARCHAR(256) NOT NULL,
                 age          INTEGER NOT NULL,
                 phone_number VARCHAR(256) NOT NULL,
                 DOB      VARCHAR(256) NOT NULL
             );'''

    cursor.execute(sql)
    db.commit()


def starting():
    print("Welcome!")
    print('''ARE YOU A :
    1.NEW USER
    2.EXISTING USER
    PLEASE ENTER YOUR CHOICE CORRESPONDING TO THE NUMBER''')

    choice = int(input())

    if choice == 1:
        new_user()
    elif choice == 2:
        existing_user()
    elif choice == 3:
        print("INVALID CHOICE ENTERED")

def new_user():

    print("Welcome to Bhanja's Bank ! We hope that both of us have a memorable experience working together!")

    print("Do you want to start a new account ? Press 1 for yes and 0 for no")

    ch = int(input())

    if ch == 1:
        create_new_user()
    else:
        print("Thank You for Visiting Us!!")

def create_new_user():

    user = []

    name = input("Enter your User Name")
    email = input("Enter your Email Address")
    age = int(input("Enter your Age"))
    address = input("Enter your address")
    starting_balance = int(input("Enter your starting balance(it should be greater than or equal to 5000):"))

    if starting_balance >= 5000:
        pass
    else:
        print("You cannot have starting balance less than Rs. 5000")
        starting_balance = int(input("Enter again:"))

    phone_number = input("Enter your Phone Number")
    dob = input("Enter your Date of Birth in DD-MM-YYYY format")

    user.append(name)
    user.append(email)
    user.append(starting_balance)
    user.append(address)
    user.append(age)
    user.append(phone_number)
    user.append(dob)

    make_db_entry_for_new_user(user)

def make_db_entry_for_new_user(details):

    sql = f"INSERT INTO users(name, email, current_balance, address, age, phone_number, DOB) VALUES('{details[0]}','{details[1]}','{details[2]}','{details[3]}','{details[4]}','{details[5]}','{details[6]}')"

    cursor.execute(sql)
    db.commit()

def existing_user():

    print("Welcome to Bhanja's Bank once again, dear customer!")
    print("We see that you are one of our existing customers ! Isnt it(enter your choice to let us know)?")

    answer = input()

    if answer == 'Yes' or answer=="YES":

        x = get_existing_customer_values()

        for details in x:

            print("Name : " + details[1])
            print("Email : " + details[2])
            print("Current Balance : " + str(details[3]))
            print("Address : " + details[4])
            print("Age : " + str(details[5]))
            print("Phone Number : " + details[6])
            print("Date of Birth : " + details[7])

            print("Are the details given above correct ?(Answer in Yes or No)")

            ans = input()

            if ans == "Yes":
                print("Thats great")
            else:
                print("Looks like your account does not exist ! Please create your account !")
                create_new_user()
    else:
        print("Perhaps you are in the wrong place . Thanks for visiting us !")


def get_existing_customer_values():

    name = input("Enter your registered name:")

    sql = f"SELECT * FROM users WHERE name='{name}'"

    cursor.execute(sql)
    db.commit()

    return cursor.fetchall()

existing_user()