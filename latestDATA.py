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


    c.execute("INSERT INTO book VALUES('1A0', 'GTA 5 GUIDE', 'Mike Smith', 2015, 'Rockstar games', 'Adventure')")
    c.execute("INSERT INTO book VALUES('2B0', 'Elden Ring THE BOOK', 'Ross Lynn', 2022, 'Bandai', 'Action RPG')")
    c.execute("INSERT INTO book VALUES('3C0', 'The Witcher 3: Wild Hunt GAME GUIDE', 'Brody Perry', 2015, 'Warner Bros.', 'Action RPG')")
    c.execute("INSERT INTO book VALUES('4D0', 'Minecraft THE BOOK', 'Notch', 2011, 'Mojang', 'Adventure')")
    c.execute("INSERT INTO book VALUES('5E0', 'Beat Saber THE BOOK', 'Ash Davis', 2019, 'Hyperbolic Magnetism', 'Rhythm')")
    conn.commit()

    c.execute("SELECT * FROM book")

    rows = c.fetchall()
    # Print header row
    booktable = ("isbn title author year publisher genre")
    print(booktable.split())
    # Print each row
    for row in rows:
        print(f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]}")
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

    c.execute("INSERT INTO product VALUES('100', 'game', 59.99, 25)")
    c.execute("INSERT INTO product VALUES('200', 'game', 29.99, 15)")
    c.execute("INSERT INTO product VALUES('300', 'game', 19.49, 5)")
    c.execute("INSERT INTO product VALUES('400', 'game', 39.99, 30)")
    c.execute("INSERT INTO product VALUES('500', 'game', 49.99, 35)")
    c.execute("INSERT INTO product VALUES('150', 'book', 14.95, 53)")
    c.execute("INSERT INTO product VALUES('250', 'book', 13.99, 65)")
    c.execute("INSERT INTO product VALUES('350', 'book', 15.99, 25)")
    c.execute("INSERT INTO product VALUES('450', 'book', 19.99, 75)")
    c.execute("INSERT INTO product VALUES('550', 'book', 29.99, 20)")
    conn.commit()

    #HAVING ISSUES WITHT THE ABOVE TABLE AND NEED TO CHANGE THE VALUES TO MATCH THE PRODUCT NUMBERS IN THE OTHER TABLES TO MAKE IT EASIER
    product_table = ("product_id category price stock")
    print(product_table.split())

    c.execute("SELECT * FROM product")
    # Fetch all rows and print them
    rows = c.fetchall()

    
    # Print each row
    for row in rows:
        print(f"{row[0]},{row[1]},{row[2]},{row[3]}")
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

    c.execute("INSERT INTO game VALUES(100, 'Grand Theft Auto 5', 2015, 'Rockstar games', 'Open-World')")
    c.execute("INSERT INTO game VALUES(200, 'Elden Ring', 2022, 'Bandai', 'Action RPG')")
    c.execute("INSERT INTO game VALUES(300, 'The Witcher 3: Wild Hunt', 2015, 'Warner Bros.', 'Action RPG')")
    c.execute("INSERT INTO game VALUES(400, 'Minecraft', 2011, 'Mojang', 'Adventure')")
    c.execute("INSERT INTO game VALUES(500, 'Beat Saber', 2019, 'Hyperbolic Magnetism', 'Rhythm')")
    conn.commit()

    c.execute("SELECT * FROM game")
    # Fetch all rows and print them
    rows = c.fetchall()
    # Print header row
    game_table = ("game_id title year publisher genre")
    print(game_table.split())
    # Print each row
    for row in rows:
        print(f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]}")
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

    print("\nPlease select an option:")
    print("1. View all items")
    print("2. View products in a category")
    print("3. View shopping cart")
    print("4. Checkout")
    print("5. View order history")
    print("6. Edit account")
    print("7. Edit shipping information")
    print("8. Edit payment information")
    print("9. Delete account")
    print("10. Logout")

    option2 = input("Enter a numerical option to continue: ")

    if option2 == "1":
    
        view_all()
    elif option2 == "2":
                
        view_products()

    elif option2 == "3":
                
        pass
    elif option2 == "4":
                
        pass
    elif option2 == "5":
                
        pass
    elif option2 == "6":
                
        pass
    elif option2 == "7":
                
        pass
    elif option2 == "8":
                
        pass
    elif option2 == "9":
        delete_acc = input("ARE YOU SURE YOU WANT TO DELETE YOUR ACCOUNT? Type 'y' for yes or 'n' to CANCEL: ")
        if delete_acc == "y":
            delete_account()
        else:
            print("Returning you home")
            ecommerce_commandline()

        pass
    elif option2 == "10":
        
        return_to_login()
    
    else: print("Invalid argument, please try again")







def view_all():
    #TABLE DATA FOR GAMES AND BOOK


    #This bottom segment for game is not displaying the table data above :( I've tried putting it in diff locations and reformatting it


    booktable = ("isbn title author year publisher genre")
    print(booktable.split())

    c.execute("SELECT * FROM book")
    rows = c.fetchall()
    # Print each row
    for row in rows:
        print(row, '\n')


    game_table = ("game_id title year publisher genre")
    print(game_table.split())

    c.execute("SELECT * FROM game")

    rows = c.fetchall()
    # Print each row
    for row in rows:
        print(row, '\n')



    
    

   

def view_products():


    product_table = ("product_id category price stock")
    print(product_table.split())

    c.execute("SELECT * FROM product ORDER BY category")

    rows = c.fetchall()

    # Print each row
    for row in rows:
        print(row, '\n')



def delete_account():
    acc_email = input("ENTER YOUR EMAIL TO CONFIRM: ")
    c.execute("DELETE FROM user WHERE email='{acc_email}'")
    conn.commit()
    print("ACCOUNT SUCCESSFULLY TERMINATED")
    LoginScreen()


    


    

#RETURNS USER TO LOGIN PAGE OPTION 10
def return_to_login():
    print("Returning you to our login page... ")
    LoginScreen()
    









#END OF ECOMMERCE_COMMANDLINE




#code will not run until this point so if you're going to declare any functions do so above this line

#MAIN
LoginScreen()
#END OF MAIN



















# Close the connection
conn.close()