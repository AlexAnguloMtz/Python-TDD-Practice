"""
Instructions:
1) Ask the user for their full name
2) Print the full name, all in upper case letters
3) Print the full name, all in lower case letters
4) Print the full name, with each word starting with 
   an upper case letter and then rest of the word in 
   lower case letters. Repeat this for all the words
"""

import string

def main():
    full_name = input('Enter your full name: ')
    print(full_name.lower())
    print(full_name.upper())
    print(string.capwords(full_name))

main()