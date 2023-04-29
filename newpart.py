import sqlite3
import random
#starting intial connection
conn = sqlite3.connect('store.db')
c = conn.cursor()


while True:
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

        pass
    elif option2 == "2":
                
        pass
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
                
        pass
    elif option2 == "10":
        print("Logging out")     
        break
    else: print("Invalid argument, please try again")




conn.close()