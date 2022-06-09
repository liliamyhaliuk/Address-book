"""
Command-line address-book program.
Using which you can browse, add, modify, delete or search for your contacts such as friends,
family and colleagues and their information such as email address and/or phone number.
Details must be stored for later retrieval.
"""

import os
import pickle
from class_address_book import AdressBook

# Check if the address_book file already exists

ADDRESS_BOOK_PATH = os.path.sep.join(["address_book", "address_book.pkl"])
print(ADDRESS_BOOK_PATH)
if os.path.isfile(ADDRESS_BOOK_PATH):
    with open(ADDRESS_BOOK_PATH, 'rb') as f:
        new_address_book = pickle.load(f)
        print(new_address_book)
        print(new_address_book.address_book)
else:
    print("Hello")
    # Create new address book
    new_address_book = AdressBook()

# Main menu
while True:
    # Get the number of action from the user
    action = input('''
    Address book menu: 
        1 - Browse in address book
        2 - Add new contact
        3 - Modify a contact
        4 - Delete a contact
        5 - Search a contact
        0 - Exit
        Your action: ''')

    # Display all contacts from the address book (browse action)
    if action == "1":
        new_address_book.browse()

    # Add new contact of the address book (add action)
    if action == "2":
        new_address_book.add_new_contact()

    # Modify contact from contact book (modify action)
    if action == "3":
        new_address_book.modify_contact()

    # Delete a contact from address book
    if action == "4":
        new_address_book.delete_contact()
  
    # Search a contact in address book
    if action == "5":
        new_address_book.search_contact()

    # Exit from the programm
    if action == "0":
        break


# Save address book for later retrieval
with open(ADDRESS_BOOK_PATH, "wb+") as f:
    pickle.dump(new_address_book, f)
    print(new_address_book.address_book)
