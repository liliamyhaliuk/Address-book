"""
Module that contains classes of the programm "address book".
"""

from class_contact import Contact

class AdressBook:
    """ The Class represents the address book."""

    # Create new address book
    address_book = {
        'friends' : {},
        'family' : {},
        'colleagues' : {}
    }


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
                print(self.address_book)
                print("Contact was added!")
                break
            except KeyError:              
                cont_group = input("Enter correct group!(friends, family, colleagues): ")
                continue
        else:
            # User riched possible amount of errors(3)
            print("Contact wasn't added!")


    def change_param(self, mod_contact, param):
        """Function modifies passed parameter of the contact"""

        mod_contact.param = input(f"Enter new {param}: ")
        res = input(f'{param} was modified. Do you want to modify another field? (yes/no): ' )
        return res


    def change_name(self, mod_contact):
        """Function modifies name of the contact"""

        old_name = mod_contact.name.lower()
        new_name = input("Enter new name: ")

        # Change the key (name of the contact) in address book dict
        for key in self.address_book.keys():

            # Add contact with new name to the dict
            if self.address_book[key].get(old_name) is not None:
                self.address_book[key][new_name.lower()] = self.address_book[key].get(old_name)

                # Delete item with old name of the contact
                del self.address_book[key][old_name]
                mod_contact.name = new_name
                break

        res = input('Name was modified. Do you want to modify another field? (yes/no): ' )
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

        # Check if the contact was found
        if isinstance(mod_contact, Contact):

            # Show all information of the found contact to the user
            print(mod_contact)

            # Start process of modifing contact
            # Continue the process of modifing until user pass no
            USER_INPUT = "yes"
            while USER_INPUT == "yes":

                mod_attr = input("What field do you want to modify?: ")
                # Modify name of the contact
                if mod_attr == "name":                  
                    USER_INPUT = self.mod_actions.get(mod_attr)(self, mod_contact)
                    continue
                # Modify email, address, phone_number of the contact
                elif mod_attr in ["email", "address", "phone_number"]:
                    USER_INPUT = self.mod_actions.get(mod_attr)(self, mod_contact, mod_attr)
                    continue
                else:
                    print("Not valid field. Enter correct modified field!")
        else:
            # Contact wasn't found. Print >> Contact does't exist
            print(mod_contact)


    def delete_contact(self):
        """Delete a contact from address book"""
        # Get the name of the contact that has to be deleted
        del_contact = input("Delete contact (Enter name): ").lower()
        
        # Find a contact in the groups of contacts
        for key in self.address_book.keys():
            if self.address_book[key].get(del_contact) is not None:
                del self.address_book[key][del_contact]
                print("Contact was deleted!")
                break
        else:
            print("Contact doesn't exist.")


    def search_contact(self):
        """Search a contact in address book"""
        s_name = input("Search for the contact (Enter name): ")
        print(self.search(s_name))
