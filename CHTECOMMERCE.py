import sqlite3
import random

#starting intial connection
conn = sqlite3.connect('store.db')
c = conn.cursor()


#all of the checks\creating tables just print the output for yall to see them working the outputs can be changed later for cleaner look


#CHECKING\CREATING USER TABLE
print('Check if USER table exists in the database:')
listOfTables = conn.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='user'; """).fetchall()
 
if listOfTables == []:
    #creating user table
    c.execute('''CREATE TABLE user
             (customer_id INTEGER PRIMARY KEY,
             email TEXT,
             password TEXT,
             name TEXT,
             phone INTEGER)''')

    conn.commit()
    c.execute("SELECT * FROM user")
    rows = c.fetchall()
    # Print header row
    usertable = ("customer_id email password name phone")
    print(usertable.split())
    # Print each row
    for row in rows:
        print(f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]}")
    #finished creating user table
else:
    print('Table found!')
#END OF CHECKING\CREATING TABLE 



#CHECKING\CREATING SHIPPING_INFO TABLE
print('Check if shipping_info table exists in the database:')
listOfTables = conn.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='shipping_info'; """).fetchall()

if listOfTables == []:
    #creating shipping info table
    c.execute('''CREATE TABLE shipping_info
                (shipping_id INTEGER PRIMARY KEY,
                address_1 TEXT,
                address_2 TEXT,
                city TEXT,
                state TEXT,
                country TEXT,
                zip INTEGER)''')

    conn.commit()
    rows = c.fetchall()
    # Print header row
    shipping_info_table = ("shipping_id address_1 address_2 city state country zip")
    print(shipping_info_table.split())
    # Print each row
    for row in rows:
        print(f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]}")
    c.execute("SELECT * FROM shipping_info")
    #finished creating shipping info table
else:   
    print('Table found!')
#END OF CHECKING\CREATING



#CHECKING\CREATING BOOK TABLE
print('Check if book table exists in the database:')
listOfTables = conn.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='book'; """).fetchall()

if listOfTables == []:
    #creating book table 
    c.execute('''CREATE TABLE book
                (isbn TEXT PRIMARY KEY,
                title TEXT,
                author TEXT,
                year INTEGER,
                publisher TEXT,
                genre TEXT)''')

    conn.commit()
    rows = c.fetchall()
    # Print header row
    booktable = ("isbn title author year publisher genre")
    print(booktable.split())
    # Print each row
    for row in rows:
        print(f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]}")
    c.execute("SELECT * FROM book")
    #finsihed creating book table
else:   
    print('Table found!')
#END OF CHECKING\CREATING


#CHECKING\CREATING CART TABLE
print('Check if cart table exists in the database:')
listOfTables = conn.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='cart'; """).fetchall()

if listOfTables == []:
    #creating cart table 
    c.execute('''CREATE TABLE cart
                (cart_id INTEGER PRIMARY KEY,
                quantity INTEGER,
                product_id INTEGER)''')
    conn.commit()
    rows = c.fetchall()
    # Print header row
    carttable =("cart_id quantity product_id")
    print(carttable.split())
    # Print each row
    for row in rows:
        print(f"{row[0]},{row[1]},{row[2]}")
    c.execute("SELECT * FROM cart")
    #finished creating cart table
else:   
    print('Table found!')
#END OF CHECKING\CREATING



#CHECKING\CREATING PAYMENT_INFO TABLE
print('Check if payment_info table exists in the database:')
listOfTables = conn.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='payment_info'; """).fetchall()

if listOfTables == []:
    #creating payment info table
    c.execute('''CREATE TABLE payment_info
                (payment_id INTEGER PRIMARY KEY,
                card_number INTEGER,
                ccv INTEGER,
                address_1 TEXT,
                address_2 TEXT,
                city TEXT,
                state TEXT,
                country TEXT,
                zip INTEGER)''')

    conn.commit()
    # Fetch all rows and print them
    rows = c.fetchall()
    # Print header row
    payment_info_table = ("payment_id card_number ccv address_1 address_2 city state country zip")
    print(payment_info_table.split())
    # Print each row
    for row in rows:
        print(f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]},{row[7]},{row[8]}")
    c.execute("SELECT * FROM payment_info")
    #finished creating payment info table
else:   
    print('Table found!')
#END OF CHECKING\CREATING



#CHECKING\CREATING PRODUCT TABLE
print('Check if product table exists in the database:')
listOfTables = conn.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='product'; """).fetchall()

if listOfTables == []:
    #creating product table
    c.execute('''CREATE TABLE product
                (product_id INTEGER PRIMARY KEY,
                category TEXT,
                price FLOAT,
                stock INTEGER)''')
    conn.commit()
    # Fetch all rows and print them
    rows = c.fetchall()
    # Print header row
    product_table = ("product_id category price stock")
    print(product_table.split())
    # Print each row
    for row in rows:
        print(f"{row[0]},{row[1]},{row[2]},{row[3]}")
    c.execute("SELECT * FROM product")
    #finsihed creating product table 
else:   
    print('Table found!')
#END OF CHECKING\CREATING



#CHECKING\CREATING GAME TABLE
print('Check if game table exists in the database:')
listOfTables = conn.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='game'; """).fetchall()

if listOfTables == []:
        #creating game table
    c.execute('''CREATE TABLE game
                (game_id INTEGER PRIMARY KEY,
                title TEXT,
                year INTEGER,
                publisher TEXT,
                genre INTEGER)''')

    conn.commit()
    # Fetch all rows and print them
    rows = c.fetchall()
    # Print header row
    game_table = ("game_id title year publisher genre")
    print(game_table.split())
    # Print each row
    for row in rows:
        print(f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]}")
    c.execute("SELECT * FROM game")
    #finished creating game table 
else:   
    print('Table found!')
#END OF CHECKING\CREATING



#CHECKING\CREATING PURCHASE TABLE
print('Check if purchase exists in the database:')
listOfTables = conn.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='purchase'; """).fetchall()

if listOfTables == []:
        #creating purchase table 
    c.execute('''CREATE TABLE purchase
                (purchase_id INTEGER PRIMARY KEY,
                user_id TEXT,
                products TEXT,
                purchase_date TEXT)''')

    conn.commit()
    # Fetch all rows and print them
    rows = c.fetchall()
    # Print header row
    purchase_table = ("purchase_id user_id products purchase_date")
    print(purchase_table.split())
    #print each row
    for row in rows:
        print(f"{row[0]},{row[1]},{row[2]},{row[3]}")
    c.execute("SELECT * FROM purchase")
    #finished creating purchase table 
else:   
    print('Table found!')
#END OF CHECKING\CREATING



#CHECKING\CREATING STORE TABLE
print('Check if store table exists in the database:')
listOfTables = conn.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='store'; """).fetchall()

if listOfTables == []:
            #creating store table
    c.execute('''CREATE TABLE store
                (store_id TEXT PRIMARY KEY,
                name TEXT,
                address_1 TEXT,
                address_2 TEXT,
                phone INTEGER,
                email TEXT)''')

    conn.commit()
    # Fetch all rows and print them
    rows = c.fetchall()
    # Print header row
    store_table = ("store_id name address_1 address_2 phone email")
    print(store_table.split())
    # Print each row
    for row in rows:
        print(f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]}")
    c.execute("SELECT * FROM store")
    #finished creating store table
else:   
    print('Table found!')
#END OF CHECKING\CREATING





#LOGIN FUNCTION
def Login():
    email = input("Enter your email address: ")
    password = input("Enter your password: ")

    c.execute("SELECT * FROM user WHERE email=? AND password=?", (email, password))
    row = c.fetchone()
    if row is None:
        print("Invalid email or password, please try again.")
    else:
        print("Login successful")
        ecommerce_commandline()

#END LOGIN FUNCTION



#CREATEACCOUNT FUNCTION
def CreateAccount():

    while True:
        customer_id = random.randint(1000, 9999)
        email = input("Enter your email: ")
        password = input("Please create a password: ")
        name = input("Enter your name: ")
        phone = int(input("Please provide a phone number: "))

        c.execute("INSERT INTO user (customer_id, email, password, name, phone) VALUES (?, ?, ?, ?, ?)",(customer_id, email, password, name, phone))
        conn.commit()

        print("Account created")

        account_creation_option = input("Enter 1 to log in or 2 to create another account: ")

        if account_creation_option == "1":
            break
        elif account_creation_option == "2":
            continue
        else:
            print("Invalid choice, please try again")

    Login()
#END CREATE ACCOUNT FUNCTION



#START OF LOGINSCREEN FUNCTION
def LoginScreen():
    #menu start options as seen in inital perameters
    print("Welcome to our shop! Please enter a number from the following list to proceed.")
    print("1. Login")
    print("2. Create an account")
    print("3. Quit")

    login_screen_option = input("Enter your choice ")

    #user selects login
    if login_screen_option == "1":

        Login()
    #user selects to create an account
    elif login_screen_option == "2": 

        CreateAccount()     
    #user selects to exit the program
    elif login_screen_option == "3":

        print("Thank you for visiting our e-shop!")
        quit()
    else:
        print("Invalid choice, please enter 1, 2 or 3 to continue")
#END OF LOGINSCREEN FUNCTION


#this below is going to be the master function for the database commandline 
#we're going to hop in and out of it after the user logs in to edit, view data ect...
#good example is the LoginScreen() function above

#dont forget to conn.commit() data like me and panda did also if yall dont get around to looking at pandas import i will <3


#START OF ECOMMERCE_COMMANDLINE
def ecommerce_commandline():
    print("you are now in the database")
#END OF ECOMMERCE_COMMANDLINE


#code will not run until this point so if you're going to declare any functions do so above this line

#MAIN
LoginScreen()
#END OF MAIN

# Close the connection
conn.close()