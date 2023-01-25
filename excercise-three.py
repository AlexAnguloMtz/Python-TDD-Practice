"""
Consider a phone with the following format: prefix-number-extension. 
The prefix is the country's code and the extension
has two digits. For example: +52-6621012345-56 
Write a program to ask the user for a phone number
with this format and show the phone with no prefix or extension
"""

def main():
    formatted_phone = input('Enter your phone number: ')
    phone = formatted_phone.split('-')[1]
    print(f'Your phone number is: {phone}')

main()