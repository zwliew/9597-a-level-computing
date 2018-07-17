#!/usr/bin/env python3

def main():
    count = {}
    for j in range(ord('a'), ord('z') + 1):
        count[chr(j)] = 0

    file = open('AIRCON.txt')

    char = file.read(1)
    while char != '':
        if char.isalpha():
            char = char.lower()
            count[char] += 1
        char = file.read(1)

    file.close()

    values_sorted = sorted(list(count.values()), reverse=True)

    PRINT_FORMAT = '{:<20} {:<20}'
    print(PRINT_FORMAT.format('Alphabet', 'Frequency'))
    printed = []
    for value in values_sorted:
        for k, v in count.items():
            if value == v and k not in printed:
                printed.append(k)
                print(PRINT_FORMAT.format(k, value))
                break

main()
