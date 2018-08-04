#!/usr/bin/env python3

# Pass in the array, the element to find, as well as the current low and high indices.
def binary_search_recursive(arr, el, lo, hi):
    # When the element does not exist in the array,
    # the low index will be greater than the high index.
    # In this case, just return -1 as it represents an invalid array index.
    if lo > hi:
        return -1

    index = (lo + hi) // 2
    if arr[index][0] == el:
        return index
    elif el < arr[index][0]:
        return binary_search_recursive(arr, el, lo, index - 1)
    else:
        return binary_search_recursive(arr, el, index + 1, hi)

def binary_search(arr, input_value, low_element, high_element):
    element_found = False
    while not element_found:
        index = (low_element + high_element) // 2
        if arr[index][0] == input_value:
            element_found = True
        elif input_value < arr[index][0]:
            high_element = index - 1
        else:
            low_element = index + 1
    return index if element_found else -1

def main():
    cities = []
    file = open('CITY.csv')
    file.readline() # Skip the first line
    for line in file:
        cities.append(line.strip().split(','))
    file.close()

    input_value = 'Istanbul'
    index = binary_search(cities, input_value, 0, len(cities) - 1)

    if index != -1:
        print(input_value, 'was found at index', index)
        print('Country:', cities[index][1])
        print('Population:', cities[index][2])
    else:
        print('Sorry,', input_value, 'could not be found.')

main()
