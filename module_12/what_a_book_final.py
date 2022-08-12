'''
Jeremy Johnson
8/4/2022
CYBR410
Assignment 11.2
'''

from time import sleep
import mysql.connector
from mysql.connector import errorcode
import sys

# database configuration for connecting to the database
config = {
    'user': 'whatabook_user',
    'password':'MySQL8IsGreat!',
    'host' : 'localhost',
    'database' : 'whatabook',
    'raise_on_warnings' : True
}


# cheesy 'loading screen' to make it seem like this tiny program is actually running something more substantial. More of a fun joke to myself than anything else...
print('Initializing.')
sleep(.3) #sleep method essentially pauses the program from moving through the code for the specified amount of time
print('Initializing..')
sleep(.5)
print('Initializing...')
sleep(.2)
print('Initialization complete!')
sleep(1)

# greet the user at the start of the application
def greeting():
    
    print('\nWelcome to the WhatABook Application!')
    menu()

# main navigation menu for users
def menu():
    print("\n -- MAIN MENU --\n")
    print("Please choose one of the options below.\n")
    print(
          "1.) List of books in stock.\n"
          "2.) WhatABook Locations.\n"
          "3.) My Account Information.\n"
          "4.) Quit Application.\n"
          )

    user_choice = input("Please enter the number of the option you would like to navigate to: \n")

# if statements for basic exception handling and directing the application to the correct code sections. Could maybe be improved with while loop.
    if user_choice.isdigit() == False: #isdigit if statement handles exceptions where a user inputs a non-digit character. 
        print("\nWhoopsie doodles, '{}' is not a number. Please try again...".format(user_choice))
        sleep(2)
        menu()
    if int(user_choice) < 1 or int(user_choice) > 4: #converting user_choice into an int prevents a TypeError from occuring when trying to less than/greater than an int and a string.  
        print("\nWhoopsie doodles, thats not a valid option. Please try again...")
        sleep(2)
        menu()
    if int(user_choice) == 1:
        book_list(cursor)
    if int(user_choice) == 2:
        locations(cursor)
    if int(user_choice) == 3:
        account_menu()
    if int(user_choice) == 4:
        print('\nHope to see you again soon!!')
        sleep(2)
        sys.exit(0) #terminates the program

# displays a list of all available books in stock.
def book_list(cursor):
    
    cursor.execute("select book_id, book_name, author, details from book")
    books = cursor.fetchall()

    print('--- Available Books ---\n')

    for book in books:
        print('Book ID: {}\nBook Name: {}\nAuthor: {}\nDetails: {}\n'.format(book[0],book[1],book[2],book[3]))

    input('Press Enter to return to the Main Menu: \n')
    menu()

# displays a list of locations for WhatABook (WAB) and the hours of operation.
def locations(cursor):
    
    cursor.execute("select store_id, locale from store")
    stores = cursor.fetchall()

    print('--- WhatABook Locations ---\n')

    for store in stores:
        print('Location: {}\n'.format(store[1]))

    input('Press Enter to return to the Main Menu:\n')
    menu()

# prompts user to enter their WAB user ID .
def account_info():

    user_num = input('\nPlease enter User ID#:\n')

# basic exception handling for incorrect input. Again a while loop would probably help with EH.
    if user_num.isdigit() == False:
        print("\nWhoopsie doodles, '{}' is not a number. Please try again...".format(user_num))
        sleep(2)
        account_menu()
    if int(user_num) < 1 or int(user_num) > 3:
        print('\nWhoopsie doodles, that is not a valid User ID#. Please try again...')
        sleep(2)
        account_menu()
    else:
        user_first = 'select first_name from user where user_id = {}'.format(int(user_num))
        cursor.execute(user_first)
        display = cursor.fetchone()
        print('\nWelcome back {}!'.format(display[0]))
        return user_num
        #returns user input back to the account_info method
        
# account menu navigation for users.
def account_menu():

    print("\n -- ACCOUNT MENU --\n")
    print("Please choose one of the options below.\n")
    print(
          "1.) View Wishlist.\n"
          "2.) Add book(s) to Wishlist.\n"
          "3.) Return to Main Menu.\n"
          "4.) Quit Application.\n"
          )

    user_choice = input("Please enter the number of the option you would like to navigate to: \n")

# if statements to guide the users to the correct sections and basic exception handling. While loops, we get it...
    if user_choice.isdigit() == False:
        print("\nWhoopsie doodles, '{}' is not a number. Please try again...".format(user_choice))
        sleep(2)
        account_menu()
    if int(user_choice) < 1 or int(user_choice) > 4:
        print("\nWhoopsie doodles, thats not a valid option. Please try again...")
        sleep(2)
        account_menu()
    if int(user_choice) == 1:
        user_id = account_info()
        wishlist(cursor, user_id)
    if int(user_choice) == 2:
        user_id = account_info()
        not_wish(cursor, user_id)
        book_id = input('Please enter the Book ID that you would like to add to your Wishlist: \n')
        add_wish(cursor, user_id, book_id)
        db.commit()
        print('Book ID: {} has been added to your Wishlist!\n'.format(book_id))
        account_menu()
    if int(user_choice) == 3:
        menu()
    if int(user_choice) == 4:
        print('\nHope to see you again soon!!')
        sleep(2)
        sys.exit(0)

# displays the users wishlist. I want to look into how to prevent duplicates in here later. 
def wishlist(cursor, user_id):
   
    cursor.execute(
        'select user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author ' +
        'from wishlist ' +
        'inner join user on wishlist.user_id = user.user_id ' +
        'inner join book on wishlist.book_id = book.book_id ' +
        'where user.user_id = {}'.format(user_id)
        )

    wishL = cursor.fetchall()

    print('\n--- Your Wishlist ---\n')

    for book in wishL:
        print('Book Name: {}\nAuthor: {}\n'.format(book[4], book[5]))

    input('\nPress Enter to return to the Account Menu.\n')
    account_menu()

# displays the books that are not currently on the users wishlist.
def not_wish(cursor, user_id):
    
    avail_book = ('select book_id, book_name, author, details from book where book_id not in (select book_id from wishlist where user_id = {})'.format(user_id))
    
    cursor.execute(avail_book)
    add_book = cursor.fetchall()

    print('--- Available Books ---')

    for book in add_book:
        print('Book ID: {}\nBook Name: {}\n'.format(book[0], book[1]))

# allows users to add books to their wishlist. Haven't been able to figure out a way to handle invalid entry on this section yet. Tried try blocks but was unable to 
# find the right exception to call and redirect.
def add_wish(cursor, user_id, book_id):
    cursor.execute('insert into wishlist(user_id, book_id) values({}, {})'.format(user_id, book_id))

# try block for catching database connection errors and to kick off the program. 
try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    greeting()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password is invalid.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)
finally:
    db.close()
