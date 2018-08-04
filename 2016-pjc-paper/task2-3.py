#!/usr/bin/env python3

def cryptograph(password, encrypt):
    encryption_key = (('a','m'),('b','h'),('c','t'),('d','f'),('e','g'),
                  ('f','k'),('g','b'),('h','p'),('i','j'),('j','w'),
                  ('k','e'),('l','r'),('m','q'),('n','s'),('o','l'),
                  ('p','n'),('q','i'),('r','u'),('s','o'),('t','x'),
                  ('u','z'),('v','y'),('w','v'),('x','d'),('y','c'),('z','a'),
                  ('0','7'),('1','3'),('2','8'),('3','9'),('4','5'),
                  ('5','6'),('6','0'),('7','1'),('8','4'),('9','2'))
    crypt_dict = {}
    for k,v in encryption_key:
        if encrypt:
            crypt_dict[k] = v
        else:
            crypt_dict[v] = k

    processed = ''
    for i in range(len(password)):
        char = password[i]
        lowered = char.lower()
        converted = char
        if lowered in crypt_dict:
            converted = crypt_dict[lowered]
        processed += converted if lowered == char else converted.upper()

    return processed

def main():
    passwords_file = open('PASSWORDS.txt')
    converted_file = open('CONVERTED.txt', 'w')

    WRITE_FORMAT = '{:29}\n'
    for line in passwords_file:
        password = line.strip()
        encrypted = cryptograph(password, True)
        converted_file.write(WRITE_FORMAT.format(encrypted))

    passwords_file.close()
    converted_file.close()

main()
