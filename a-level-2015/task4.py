#!/usr/bin/env python3

class PrintJob:
    def __init__(self, user_id, terminal, size):
        self.user_id = user_id
        self.terminal = terminal
        self.size = size

class PrintQueue:
    def __init__(self):
        self.__jobs = []

def validate_user_id(user_id):
    if len(user_id) != 9:
    	return 1
    
    if not user_id[5:].isdecimal():
        return 2

    if not user_id.startswith('2015_'):
    	return 3

    return 0

def main():
    user_id = input('Enter a user ID: ').strip()
    validated = validate_user_id(user_id)
    if validated != 0:
        print('Invalid user ID.', end=' ')
    if validated == 1:
    	print('The user ID is not 9 characters in length.')
    elif validated == 2:
    	print('The last 4 digits of the user ID are not all decimal digits.')
    elif validated == 3:
	    print('The user ID is not prefixed with "2015_".')

main()
