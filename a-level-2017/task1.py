#!/usr/bin/env python3

def main():
    inventory = []
    item_counts = {}

    with open('INVENTORY.txt') as file:
        for line in file:
            item = line.rstrip()
            inventory.append(item)
            if item not in item_counts:
                item_counts[item] = 0
            else:
                item_counts[item] += 1
    
    PRINT_FMT = '{:<20} {:<10}'
    print(PRINT_FMT.format('ItemType', 'Count'))
    for k,v in item_counts.items():
        print(PRINT_FMT.format(k, v))

main()
