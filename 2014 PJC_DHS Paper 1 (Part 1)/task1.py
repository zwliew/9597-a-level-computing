#!/usr/bin/env python3

def one():
    print('{:10}\t{:10}\t{:20}\t{:10}'.format('Runner ID', 'Country', 'Name', 'Race Time'))
    with open('RACE.csv') as file:
        for line in file:
            data = line.strip().split(',')
            if float(data[3]) > 11:
                print('{:10}\t{:10}\t{:20}\t{:10}'.format(data[0], data[1], data[2], data[3]))

def two():
    print('{:10}\t{:10}\t{:20}\t{:10}'.format('Runner ID', 'Country', 'Name', 'Race Time'))
    with open('RACE.csv') as file:
        runners = []
        for line in file:
            runners.append(line.strip().split(','))

        runners.sort(key=lambda item: item[3])
        rank = 0
        count = 0
        prev_time = -1
        while rank < 11:
            if prev_time != runners[count][3]:
                prev_time = runners[count][3]
                rank += 1
            if rank < 11:
                print('{:10}\t{:10}\t{:20}\t{:10}'.format(runners[count][0], runners[count][1], runners[count][2], runners[count][3]))
            count += 1

def main():
    one()
    two()

main()
