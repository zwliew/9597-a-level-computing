#!/usr/bin/env python3

def HashKey(ThisCountry):
    total = 0
    for char in ThisCountry:
        total += ord(char)
    return (total % 373) + 1

def CreateCountry():
    with open('NEWFILE', 'r+') as new_file:
        new_file.write((' ' * 39 + '\n') * 373)
        with open('COUNTRIES.txt') as countries_file:
            country_name = countries_file.readline()
            population = countries_file.readline()
            while len(country_name) > 0:
                country_name = country_name.strip()
                population = population.strip()
                address = HashKey(country_name) - 1

                new_file.seek(address * 40)
                # Upon collision, sequentially iterate through each subsequent
                # address to find an empty line
                while len(new_file.readline().strip()) != 0:
                    address += 1
                new_file.seek(address * 40)

                new_file.write('{:<30}{:<9}\n'.format(country_name, population))

                country_name = countries_file.readline()
                population = countries_file.readline()

def LookUpCountry():
    name = input('Input a country name: ')
    address = HashKey(name) - 1
    with open('NEWFILE') as file:
        file.seek(address * 40)
        stored_name = None
        while name != stored_name:
            info = file.readline().strip().split()
            stored_name = ''.join(info[:len(info) - 1])
            address += 1

        population = info[1]
        print('Country name:', name)
        print('Population:', population)
        print('Address:', address)

def main():
    CreateCountry()
    LookUpCountry()

main()