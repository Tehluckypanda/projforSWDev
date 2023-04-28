import sqlite3
import random
#starting intial connection
conn = sqlite3.connect('store.db')
c = conn.cursor()

#c.execute('''CREATE TABLE user
#             (customer_id INTEGER PRIMARY KEY,
#             email TEXT,
#             password TEXT,
#             name TEXT,
#             phone INTEGER)''')

#conn.commit()




c.execute("SELECT * FROM user")


rows = c.fetchall()

# Print header row
print("customer_id\temail\tpassword\tname\tphone")

# Print each row
for row in rows:
    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}")


#c.execute('''CREATE TABLE shipping_info
#             (shipping_id INTEGER PRIMARY KEY,
#             address_1 TEXT,
#             address_2 TEXT,
#             city TEXT,
#             state TEXT,
#             country TEXT,
#             zip INTEGER)''')

#conn.commit()


rows = c.fetchall()

# Print header row
print("shipping_id\taddress_1\taddress_2\tcity\tstate\tcountry\tzip")

# Print each row
for row in rows:
    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}")

c.execute("SELECT * FROM shipping_info")

#c.execute('''CREATE TABLE cart
#             (cart_id INTEGER PRIMARY KEY,
#             quantity INTEGER,
#             product_id INTEGER)''')

#conn.commit()


rows = c.fetchall()

# Print header row
print("cart_id\tquantity\tproduct_id")

# Print each row
for row in rows:
    print(f"{row[0]}\t{row[1]}\t{row[2]}")

c.execute("SELECT * FROM cart")

#c.execute('''CREATE TABLE book
#             (isbn TEXT PRIMARY KEY,
#             title TEXT,
#             author TEXT,
#             year INTEGER,
#             publisher TEXT,
#             genre TEXT)''')

#conn.commit()



rows = c.fetchall()

# Print header row
print("isbn\ttitle\tauthor\tyear\tpublisher\tgenre")

# Print each row
for row in rows:
    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}")

c.execute("SELECT * FROM book")

#c.execute('''CREATE TABLE payment_info
#             (payment_id INTEGER PRIMARY KEY,
#             card_number INTEGER,
#             ccv INTEGER,
#             address_1 TEXT,
#             address_2 TEXT,
#             city TEXT,
#             state TEXT,
#             country TEXT,
#             zip INTEGER)''')

#conn.commit()




# Fetch all rows and print them
rows = c.fetchall()

# Print header row
print("payment_id\tcard_number\tccv\taddress_1\taddress_2\tcity\tstate\tcountry\tzip")

# Print each row
for row in rows:
    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}\t{row[7]}\t{row[8]}")

c.execute("SELECT * FROM payment_info")

#c.execute('''CREATE TABLE product
#             (product_id INTEGER PRIMARY KEY,
#             category TEXT,
#             price FLOAT,
#             stock INTEGER)''')

#conn.commit()



# Fetch all rows and print them
rows = c.fetchall()

# Print header row
print("product_id\tcategory\tprice\tstock")

# Print each row
for row in rows:
    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")

c.execute("SELECT * FROM product")

#c.execute('''CREATE TABLE game
#             (game_id INTEGER PRIMARY KEY,
#             title TEXT,
#             year INTEGER,
#             publisher TEXT,
#             genre INTEGER)''')

#conn.commit()



# Fetch all rows and print them
rows = c.fetchall()

# Print header row
print("game_id\ttitle\tyear\tpublisher\tgenre")

# Print each row
for row in rows:
    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}")

c.execute("SELECT * FROM game")

#c.execute('''CREATE TABLE purchase
#             (purchase_id INTEGER PRIMARY KEY,
#             user_id TEXT,
#             products TEXT,
#             purchase_date TEXT)''')

#conn.commit()



# Fetch all rows and print them
rows = c.fetchall()

# Print header row
print("purchase_id\tuser_id\tproducts\tpurchase_date")

for row in rows:
    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")

c.execute("SELECT * FROM purchase")

#c.execute('''CREATE TABLE store
#             (store_id TEXT PRIMARY KEY,
#             name TEXT,
#             address_1 TEXT,
#             address_2 TEXT,
#             phone INTEGER,
#             email TEXT)''')

#conn.commit()



# Fetch all rows and print them
rows = c.fetchall()

# Print header row
print("store_id\tname\taddress_1\taddress_2\tphone\temail")

# Print each row
for row in rows:
    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}")


c.execute("SELECT * FROM store")





#menu start options as seen in inital perameters
print("Welcome to our shop! Please enter a number from the following list to proceed.")
print("1. Login")
print("2. Create an account")
print("3. Quit")

option = input("Enter your choice")
#data in table
c.execute("INSERT INTO user VALUES (1, 'JohnSmith@gmail.com', 'password', 'John Smith', 111-111-1111)")

if option == "1":

    email = input("Enter your email address: ")
    password = input("Enter your password: ")

    c.execute("SELECT * FROM user WHERE email=? AND password=?", (email, password))
    row = c.fetchone()
    if row is None:
        print("Invalid email or password, please try again.")
    else:
        print("Login successful")

elif option == "2":
   while True:
    customer_id = random.randint(1000, 9999)
    email = input("Enter your email: ")
    password = input("Please create a password: ")
    name = input("Enter your name: ")
    phone = int(input("Please provide a phone number: "))

    c.execute("INSERT INTO user (customer_id, email, password, name, phone) VALUES (?, ?, ?, ?, ?)",(customer_id, email, password, name, phone))
    print("Account created")

    option = input("Enter 1 to log in or 2 to create another account: ")

    if option == "1":

        break
    elif option == "2":

        continue
    else:

        print("Invalid choice, please try again")
        break

elif option == "3":

    print("Thank you for visiting our e-shop!")
    quit()

else:
    print("Invalid choice, please enter 1, 2 or 3 to continue")






# Close the connection
conn.close()