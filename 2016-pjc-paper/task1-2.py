#!/usr/bin/env python3

def main():
    files = ['AIRCON.txt', 'BLIND.txt', 'COMP.txt', 'EMPEROR.txt']
    counts = []

    for i in files:
        count = {}
        for j in range(ord('a'), ord('z') + 1):
            count[chr(j)] = 0

        file = open(i)

        char = file.read(1)
        while char != '':
            if char.isalpha():
                char = char.lower()
                count[char] += 1
            char = file.read(1)

        counts.append(count)

        file.close()

    PRINT_FORMAT = '{:<20} {:<20} {:<20} {:<20} {:<20}'
    aircon, blind, comp, emperor = files
    print(PRINT_FORMAT.format('Alphabet', aircon, blind, comp, emperor))
    for i in range(ord('a'), ord('z') + 1):
        char = chr(i)
        aircon = counts[0][char]
        blind = counts[1][char]
        comp = counts[2][char]
        emperor = counts[3][char]
        print(PRINT_FORMAT.format(char, aircon, blind, comp, emperor))

main()
