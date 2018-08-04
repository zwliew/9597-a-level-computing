#!/usr/bin/env python3

def main():
    print('1. Read file data')
    print('2. Bubble sort')
    print('3. Quick sort / Insertion sort')
    print('4. End')

    option = int(input('Enter your option: '))

    admissions = []
    while option != 4:
        if option != 1 and option != 2 and option != 3: # or not in (1, 2, 3, 4)
            print('Invalid option. Please pick an option from 1 to 4.')
            option = int(input('Enter your option: '))
            continue

        if option == 1:
            admissions = []
            with open('ADMISSIONS-DATA.txt') as file:
                day = 0
                for line in file:
                    total = int(line.strip())
                    admissions.append((day, total))
                    day += 1

        elif option == 2:
            count = 0
            swapped = True
            end = len(admissions)
            while swapped:
                swapped = False
                for i in range(1, end):
                    count += 1
                    print(count)
                    if admissions[i - 1][1] > admissions[i][1]:
                        tmp = admissions[i]
                        admissions[i] = admissions[i - 1]
                        admissions[i - 1] = tmp
                        swapped = True
                end -= 1

            PRINT_FMT = '{:<10} {:<15}'
            print(PRINT_FMT.format('Day no.', 'Admissions'))
            for day, total in admissions:
                print(PRINT_FMT.format(day, total))
            print('No. of comparisons:', count)

        elif option == 3:
            # Sort using insertion sort
            count = 0
            for i in range(1, len(admissions)):
                cur = admissions[i]
                j = i
                while j > 0 and admissions[j - 1][1] > cur[1]:
                    count += 1
                    admissions[j] = admissions[j - 1]
                    j -= 1
                admissions[j] = cur

            PRINT_FMT = '{:<10} {:<15}'
            print(PRINT_FMT.format('Day no.', 'Admissions'))
            for day, total in admissions:
                print(PRINT_FMT.format(day, total))
            print('No. of comparisons:', count)

        option = int(input('Enter your option: '))

main()
