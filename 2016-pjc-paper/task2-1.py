#!/usr/bin/env python3

def main():
    encryption_key = (('a','m'),('b','h'),('c','t'),('d','f'),('e','g'),
                  ('f','k'),('g','b'),('h','p'),('i','j'),('j','w'),
                  ('k','e'),('l','r'),('m','q'),('n','s'),('o','l'),
                  ('p','n'),('q','i'),('r','u'),('s','o'),('t','x'),
                  ('u','z'),('v','y'),('w','v'),('x','d'),('y','c'),('z','a'),
                  ('0','7'),('1','3'),('2','8'),('3','9'),('4','5'),
                  ('5','6'),('6','0'),('7','1'),('8','4'),('9','2'))

    encryption_dict = {}
    decryption_dict = {}
    for k,v in encryption_key:
        encryption_dict[k] = v
        decryption_dict[v] = k

    print('1. Encrypt a password.')
    print('2. Decrypt a password.')
    choice = input('Pick either option 1 or 2: ')
    while choice != '1' and choice != '2':
        print('Invalid choice. Please pick either option 1 or 2.')
        choice = input('Pick either option 1 or 2: ')

    password = input('Please input your password: ')
    processed = ''
    for i in range(len(password)):
        char = password[i]
        lowered = char.lower()
        converted = char
        if choice == '1':
            if lowered in encryption_dict:
                converted = encryption_dict[lowered]
        else:
            if lowered in decryption_dict:
                converted = decryption_dict[lowered]
        processed += converted if lowered == char else converted.upper()

    if choice == '1':
        print('Encrypting your password', password, 'gives', processed)
    else:
        print('Decrypting your password', password, 'gives', processed)

main()
