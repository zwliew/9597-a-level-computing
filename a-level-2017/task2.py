#!/usr/bin/env python3

def calc_check_digit(number, total):
    if len(number) > 1:
        digit = int(number[:1])
        total += (digit * (len(number) + 1))
        new_number = number[1:]
        check_digit = calc_check_digit(new_number, total)
    else:
        digit = int(number[:1])
        total += (digit * (len(number) + 1))
        calc_modulus = total % 11
        check_value = 11 - calc_modulus
        if check_value == 11:
            return '0'
        elif check_value == 10:
            return 'X'
        else:
            return str(check_value)
    if len(number) == 9:
        return number + check_digit
    else:
        return check_digit

def main():
    isbns = []
    
    with open('ISBNPRE.txt') as file:
        for line in file:
            isbns.append(line.rstrip())
    
    PRINT_FMT = '{:<15} {:<15}'
    print(PRINT_FMT.format('Original', 'Fixed'))
    for isbn in isbns:
        fixed = calc_check_digit(isbn, 0)
        print(PRINT_FMT.format(isbn, fixed))

main()