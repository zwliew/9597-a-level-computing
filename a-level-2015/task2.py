#!/usr/bin/env python3

def converter(denary_number, accumulator):
    if denary_number == 0 or denary_number == 1:
        accumulator += str(denary_number)
        print(accumulator[::-1]) # Reverse the string
    else:
        accumulator += str(denary_number % 2)
        converter(denary_number // 2, accumulator)

def main():
    converter(173, '')

main()
