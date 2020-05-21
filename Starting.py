from tkinter import *
import sqlite3
import os
from tkinter.font import Font


def home():

    root = Tk()
    root.state("zoomed")
    root.configure(background="#ECE5DD")

    fontFamily = StringVar(value="Verdana")
    fontSize = IntVar(value=20)

    appfont = Font(family=fontFamily.get(), size=fontSize.get(), weight='bold')

    Label(root,text="WELCOME TO BHANJA BANK!", bg="#ECE5DD", font=appfont).place(relx=0.35,rely=0.025)

    Label(root,text="GOOD TO SEE YOU HERE !", bg="#ECE5DD",font=)
    root.mainloop()


def starting():