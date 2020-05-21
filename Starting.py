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

    if ch == '1':
        create_new_user()
    else:
        print("Thank You for Visiting Us!!")

def create_new_user():


def existing_user():
    pass

