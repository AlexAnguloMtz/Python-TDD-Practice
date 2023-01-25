import re

"""
Consider a phone with the following format: prefix-number-extension. 
The prefix is the country's code and the extension
has two digits. For example: +52-6621012345-56 
Write a program to ask the user for a phone number
with this format and show the phone with no prefix or extension
"""

"""
Immutable class to represent a Phone.
A Phone has 3 parts: prefix, value and extension.
Each of these parts is a field in this class.
"""
class Phone:

    _PHONE_REGEX = '^[+]?[\d]{2}-[\d]{1,10}-[\d]{2}$'
    _PATTERN = re.compile(_PHONE_REGEX)

    def __init__(self, formatted_phone):
        self.validate(formatted_phone)
        phone_parts = formatted_phone.split('-')
        self._prefix = phone_parts[0]
        self._value = phone_parts[1]
        self._extension = phone_parts[2]
    
    def validate(self, formatted_phone):
        if (not self._PATTERN.match(formatted_phone)):
            raise Error(f'Invalid phone: {formatted_phone}')

    @property
    def prefix(self):
        return self._prefix

    @property
    def value(self):
        return self._value

    @property
    def extension(self):
        return self._extension

def main():
    phone = Phone(input('Enter your phone number: '))
    print(f'Your phone number is: {phone.value}')

main()

