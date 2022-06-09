"""
Module that contains classes of the programm "address book".
"""

from dataclasses import dataclass

@dataclass
class Contact:
    """ The Class represents the contact from the address-book."""
    name: str = 'Undefined'
    email: str = ""
    address: str = ""
    phone_number: str = ""
