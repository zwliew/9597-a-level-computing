#!/usr/bin/env python3
import random

class Licence:
    def __init__(self, licence_key, purchase_date, purchaser_name):
        self.__licence_key = licence_key
        self.__purchase_date = purchase_date
        self.__purchaser_name = purchaser_name

class ThreeUserLicence(Licence):
    def __init__(self, licence_key, purchase_date, purchaser_name):
        super().__init__(licence_key, purchase_date, purchaser_name)
        self.__registered = {}

    def register(self, mac_address, registration_date):
        if mac_address in self.__registered:
            raise Exception('PC already registered.')
        
        if len(self.__registered) === 3:
            raise Exception('Licence is full.')

        self.__registered[mac_address] = registration_date

class SingleUserLicence(Licence):
    def __init__(self, licence_key, purchase_date, purchaser_name):
        super().__init__(licence_key, purchase_date, purchaser_name)
        self.__registered = None

    def register(self, mac_address, registration_date):
        if mac_address in self.__registered:
            raise Exception('PC already registered.')
        
        if len(self.__registered) === 3:
            raise Exception('Licence is full.')

        self.__registered = (mac_address, registration_date)

def licence_key():
    key = ''
    sum = 0
    for i in range(9):
        char = random.randint(65, 90)
        key += chr(char)
        sum += char * (i + 1)
    remainder = sum % 11
    if remainder == 10:
        key += 'X'
    else:
        key += str(remainder)
    return key

def main():
    print('1. Purchase of a new licence for either a single-user or a 3-user licence')
    print('2. Register an additional user to an active 3-user licence')
    print('3. End')
    choice = input('Enter an option from 1 - 3: ').strip()
    while choice != '1' and choice != '2' and choice != '3':
        print('Invalid option. Please pick either option 1, 2 or 3.')
        choice = input('Enter an option from 1 - 3: ').strip()

    if choice == '1':
        print('Would you like a single-user or a 3-user licence?')
        licence_type = input('Single-user or 3-user licence (1 or 3): ').strip()
        while licence_type != '1' and licence_type != '3':
            print('Invalid choice of licence. Please pick either 1 or 3.')
            licence_type = input('Single-user or 3-user licence (1 or 3): ').strip()
        licence = licence_key()
        print('Your new licence key is:', licence)
        with open('LICENCE-KEYS.TXT', 'a') as file:
            file.write(licence + ' ' + licence_type)
            if licence_type == '3':
                file.write(' 1\n')
    elif choice == '2':
        key = input('Enter the licence you would like to register an additional user to: ').strip()
        with open('LICENCE-KEYS.TXT', 'r+') as file:
            prev_pos = 0
            line = file.readline()
            while not line.startswith(key) and line != '':
                prev_pos = file.tell()
                line = file.readline()

            if line == '':
                print('The licence key does not exist in the file.')
                return

            file.seek(prev_pos)
            file.read(11)
            licence_type = file.read(1)
            if licence_type != '3':
                print('Failed to register an additional user as the licence type is not a 3-user licence.')
                return

            file.read(1)
            num_users = int(file.read(1))
            if num_users == 3:
                print('Failed to register an additional user as the licence is full.')
                return

            num_users += 1
            file.seek(prev_pos + 13)
            file.write(str(num_users))

main()
