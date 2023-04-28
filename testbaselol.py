import sqlite3
import random
#starting intial connection
conn = sqlite3.connect('store.db')
c = conn.cursor()

#menu start options as seen in inital perameters
print("Welcome to our shop! Please enter a number from the following list to proceed.")
print("1. Login")
print("2. Create an account")
print("3. Quit")

option = input("Enter your choice")
#data in table
c.execute("INSERT INTO test VALUES (1, 'JohnSmith@gmail.com', 'password', 'John Smith', 111-111-1111)")

if option == "1":

    email = input("Enter your email address: ")
    password = input("Enter your password: ")

    c.execute("SELECT * FROM test WHERE email=? AND password=?", (email, password))
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

    c.execute("INSERT INTO test (customer_id, email, password, name, phone) VALUES (?, ?, ?, ?, ?)",(customer_id, email, password, name, phone))
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

#c.execute('''CREATE TABLE test
#             (customer_id INTEGER PRIMARY KEY,
#             email TEXT,
#             password TEXT,
#             name TEXT,
#             phone INTEGER)''')

#conn.commit()




c.execute("SELECT * FROM test")


rows = c.fetchall()

# Print header row
print("customer_id\temail\tpassword\tname\tphone")

# Print each row
for row in rows:
    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}")




# Close the connection
conn.close()
