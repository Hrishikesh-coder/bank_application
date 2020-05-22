
#Bank Management Application built using SQLite3

import sqlite3

db = sqlite3.connect(f'user_details_database.db')
cursor = db.cursor()



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

    print("Do you want to start a new account ? Enter yes or no")

    ch = input()

    if 'y' in ch or 'Y' in ch:
        create_new_user()
    elif 'n' in ch or 'N' in ch:
        print("Do you want to exit ?")
        inp = input()

        if 'y' in inp or 'Y' in inp:
            exit(0)

        elif 'n' in inp or 'N' in inp:
            print("We are redirecting you to our home screen")
            starting()

        else:
            print("INVALID CHOICE ENTERED")

    else:
        print("INVALID CHOICE ENTERED")

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

    print("Your Account has been Successfully Created ! Now try logging in !")

    existing_user()

def make_db_entry_for_new_user(details):

    sql = f"INSERT INTO users(name, email, current_balance, address, age, phone_number, DOB) VALUES('{details[0]}','{details[1]}','{details[2]}','{details[3]}','{details[4]}','{details[5]}','{details[6]}')"

    cursor.execute(sql)
    db.commit()

def existing_user():

    print("Welcome to Bhanja's Bank once again, dear customer!")
    print("We see that you are one of our existing customers ! Isnt it(enter your choice to let us know)?")

    answer = input()

    if 'Y' in answer or 'y' in answer:

        x = get_existing_customer_values()

        if len(x) == 0:

            print("You do not have an account !! Create one now !")

            create_new_user()

        else :
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
                    print("Do you want to perform some action on your account ?")
                    a = input()

                    if a == "Yes" or a == "YES":
                        print('''
                            WHAT ACTION DO YOU WANT TO PERFORM ? SELECT FROM THE BELOW OPTIONS:
                            1.CHANGE ACCOUNT DETAILS
                            2.WITHDRAW MONEY
                            3.DEPOSIT MONEY
                            4.DELETE YOUR ACCOUNT
                            ''')

                        option = input("Enter your choice :")

                        if option == '1':

                            status = change_account_details(details[1])
                            print(status)

                        elif option == '2':

                            withdraw_money(details[1])

                        elif option == '3':

                            deposit_money(details[1])

                        elif option == '4':

                            delete_account(details[1])

                        else:
                            print("Invalid choice entered !")

                    else:
                        print("Thank You for visiting us ! Bye !")

    elif 'n' in answer or 'N' in answer:
            print("Perhaps you are in the wrong place . We are redirecting you to the home screen")
            starting()


def get_existing_customer_values():

    name = input("Enter your registered name:")

    sql = f"SELECT * FROM users WHERE name='{name}'"

    cursor.execute(sql)
    db.commit()



    return cursor.fetchall()

def change_account_details(name):

    sql = f"SELECT * FROM users WHERE name='{name}'"
    cursor.execute(sql)

    detail_to_change = input("Enter what should be changed : ")
    new_value = input("Enter the new value : ")

    if cursor.fetchone():
        sql = f"UPDATE users SET '{detail_to_change}' ='{new_value}' WHERE name='{name}'"
        cursor.execute(sql)
        db.commit()

    return "Succesfully Made the changes"

def withdraw_money(name):
    sql = f"SELECT * FROM users WHERE name='{name}'"
    cursor.execute(sql)

    x = cursor.fetchall()

    current_balance = x[0][3]

    amount = int(input("Enter the amount to withdraw :"))

    if int(current_balance) > 0:

        new_balance = int(current_balance) - amount

        sql = f"UPDATE users SET current_balance ='{new_balance}' WHERE name='{name}'"
        cursor.execute(sql)
        db.commit()

        print("Successfully Withdrawed the money")
        starting()

    else:
        print("Amount cannot be withdrawn! Current Balance is Rs. 0")
        starting()


def deposit_money(name):
    sql = f"SELECT * FROM users WHERE name='{name}'"
    cursor.execute(sql)

    x = cursor.fetchall()

    current_balance = x[0][3]

    amount = int(input("Enter the amount to deposit :"))

    new_balance = int(current_balance) + amount

    sql = f"UPDATE users SET current_balance ='{new_balance}' WHERE name='{name}'"
    cursor.execute(sql)
    db.commit()

    print("Successfully Deposited the money")

    starting()

def delete_account(name):

    sql = f"DELETE FROM users WHERE name='{name}'"

    cursor.execute(sql)
    db.commit()

starting()