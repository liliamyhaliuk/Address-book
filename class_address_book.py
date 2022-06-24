"""
Module that contains classes of the programm "address book".
"""

from class_contact import Contact

class AdressBook:
    """ The Class represents the address book."""

    def __init__(self, new_address_book = ""):

        # Create new address book if one doesn't exist
        if new_address_book == "":
            new_address_book = {
            'friends' : {},
            'family' : {},
            'colleagues' : {}
            }

        self.address_book = new_address_book


    def search(self, contact_name):
        """Function search for an instance of the contact with passed name"""

        contact_name = contact_name.lower()
        for contact_group in self.address_book:
            if self.address_book[contact_group].get(contact_name) is not None:
                return self.address_book[contact_group].get(contact_name)
        return "Contact doesn't exist."


    def browse(self):
        """Display all contacts from the address book (browse action)"""

        for key, value in self.address_book.items():
            # Print group of contacts
            print(f"{key}: ")

            for contact in value.values():
                # Print all contacts in the current group
                print(f" {contact}")


    def add_new_contact(self):
        """Add new contact of the address book (add action)"""

        # Get all attributes of contact from the user
        cont_name = input("Name of the new contact: ")

        # Check if contact already exists
        if self.search(cont_name) != "Contact doesn't exist.":
            print("Contact already exists.")
        else:
            # Check entered name
            if self.check_name(cont_name) == "Error":
                print("Empty name! Contact wasn't added.")
            else:
                cont_email = input("Email of the new contact: ")
                cont_adress = input("Address of the new contact: ")
                cont_phone_number = input("Phone number for the new contact: ")
                cont_group = input("Group of the contact(friends, family, colleagues): ")

                # Create new contact
                new_contact = Contact(cont_name, cont_email, cont_adress, cont_phone_number)

                # Check correctnes of the entered group name
                for error in range(2):
                    try:
                        # Add new contact to the address book
                        self.address_book[cont_group][new_contact.name.lower()] = new_contact
                        print("Contact was added!")
                        break
                    except KeyError:              
                        cont_group = input("Enter correct group!(friends, family, colleagues): ")
                        continue

                # User riched possible amount of errors(3)
                else:
                    print("Contact wasn't added!")

    def check_name(self, inp_name):
        """Function checks entered name"""

        # Cut all spaces
        inp_name = inp_name.strip()
        if inp_name == "":
            # Give last chance to enter correct name
            inp_name = input("Emptiness! Enter name (or contact won't be added): ")
            if inp_name == "":
                return "Error"


        return inp_name

    def change_param(self, mod_contact, param):
        """Function modifies passed parameter of the contact"""

        inp = input(f"Enter new {param}: ")
        # Set new value for the parameter of the contact
        setattr(mod_contact, param, inp )
        res = input(f'{param} was modified. Do you want to modify another field? (yes/no): ' )
        return res


    def change_name(self, mod_contact, mod_attr):
        """Function modifies name of the contact"""

        old_name = mod_contact.name.lower()
        new_name = input(f"Enter new {mod_attr}: ")

        # Check entered name
        if self.check_name(new_name) == "Error":
            print("Empty name! Name wasn't changed.")
        else:
            # Change the key (name of the contact) in address book dict
            for key in self.address_book.keys():

                # Add contact with new name to the dict
                if self.address_book[key].get(old_name) is not None:
                    self.address_book[key][new_name.lower()] = self.address_book[key].get(old_name)

                    # Delete item with old name of the contact
                    del self.address_book[key][old_name]
                    mod_contact.name = new_name

            res = input(f"{mod_attr} was modified. Do you want to modify another field? (yes/no): ")
            return res


    # Dict for dispatcher for changing parameters of contact
    mod_actions = {
        'name' : change_name,
        'email' : change_param,
        'address': change_param,
        'phone_number' : change_param
        }


    def modify_contact(self):
        """Modify contact from contact book (modify action)"""

        # Get the name of the contact for search
        mod_contact = input("Modify the contact (Enter name): ")
        # Search for the contact with name that user entered
        mod_contact = self.search(mod_contact)

        # Show found information about contact to the user
        print(mod_contact)

        # Check if the contact was found
        if isinstance(mod_contact, Contact):

            # Start process of modifing contact
            # Continue the process of modifing until user pass no
            USER_INPUT = "yes"

            # Error counter. In case user entered not existed field
            error_count = 0

            while USER_INPUT == "yes":

                mod_attr = input("What field do you want to modify?: ")

                # Modify name, email, address, phone_number of the contact
                if mod_attr in ["name", "email", "address", "phone_number"]:
                    USER_INPUT = self.mod_actions.get(mod_attr)(self, mod_contact, mod_attr)
                    continue

                # In case user entered not existed field
                if error_count < 3:
                    print("Not valid field. Enter correct modified field!")
                    error_count += 1
                else:
                    print("Too many incorrect inputs!")
                    break


    def delete_contact(self):
        """Delete a contact from address book"""

        # Get the name of the contact that has to be deleted
        del_contact = input("Delete contact (Enter name): ").lower()
    
        # Find a contact in the groups of contacts
        for key in self.address_book.keys():
            if self.address_book[key].get(del_contact) is not None:
                del self.address_book[key][del_contact]

                return print("Contact was deleted!")
       
        return print("Contact doesn't exist.")


    def search_contact(self):
        """Search a contact in address book"""
        s_name = input("Search for the contact (Enter name): ")
        print(self.search(s_name))
