"""
A Phone object is an immutable Value Object with 3 parts:
prefix, value and extension, separated by hyphens. 
Each of these parts is a field in this class.
"""
import re

class Phone:

    _PHONE_REGEX = '^[+]?[\d]{2}-[\d]{10}-[\d]{2}$'
    _PATTERN = re.compile(_PHONE_REGEX)

    def __init__(self, formatted_phone):
        self.validate(formatted_phone)
        phone_parts = formatted_phone.split('-')
        self._prefix = phone_parts[0]
        self._value = phone_parts[1]
        self._extension = phone_parts[2]
    
    def validate(self, formatted_phone):
        if (not (isinstance(formatted_phone, str))):
            raise TypeError('Phone must be a string')
        if (not self.is_valid_phone(formatted_phone)):
            raise InvalidPhoneException(f'Invalid phone: {formatted_phone}')

    def is_valid_phone(self, formatted_phone):
        return self._PATTERN.match(formatted_phone)

    @property
    def prefix(self):
        return self._prefix

    @property
    def value(self):
        return self._value

    @property
    def extension(self):
        return self._extension
    
class InvalidPhoneException(Exception):
    pass