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

if os.path.isfile(ADDRESS_BOOK_PATH):
    with open(ADDRESS_BOOK_PATH, 'rb') as f:
        new_address_book = pickle.load(f)
else:
    print("Hello")
    # Create new address book
    new_address_book = AdressBook()
    
# List of possible actions for menu
actions = {
    "1" : new_address_book.browse,
    "2" : new_address_book.add_new_contact,
    "3" : new_address_book.modify_contact,
    "4" : new_address_book.delete_contact,
    "5" : new_address_book.search_contact,
}

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

    # Exit from the programm
    if action == "0":
        break
    # Find and do chosen action
    try:
        actions.get(action)()
    except KeyError:
        print("Action does't exist")
        continue


# Save address book for later retrieval
with open(ADDRESS_BOOK_PATH, "wb+") as f:
    pickle.dump(new_address_book, f)
