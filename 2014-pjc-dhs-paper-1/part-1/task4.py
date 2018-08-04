#!/usr/bin/env python3

def abbreviate_ipv6(long_ipv6):
    sections = long_ipv6.strip().split(':')
    result = []

    # Strip leading zeroes from each section
    for section in sections:
        section = section.lstrip('0')
        if len(section) == 0:
            section = '0'
        result.append(section)
    result = ':'.join(result)

    # Replace consecutive sections of zeroes
    consecutive_start = result.find('0:0')
    if consecutive_start > -1:
        length_before = len(result)
        # Consecutive_start may actually be part of the end of a section
        if consecutive_start != 0 and result[consecutive_start - 1] != ':':
            consecutive_start += 2
        consecutive_end = result.rfind('0:0') + 3 # len(result) - result[::-1].find('0:0')
        result = result[:consecutive_start] + result[consecutive_end:]
        if consecutive_start == 0:
            result = ':' + result
        elif consecutive_end == length_before:
            result = result + ':'

    return result

def expand_ipv6(short_ipv6):
    sections = short_ipv6.strip().split(':')
    result = []

    # Fill in leading zeroes in each section
    consecutive_start = -1
    for i in range(len(sections)):
        section = sections[i]
        if len(section) == 0:
            consecutive_start = i
        section = section.rjust(4, '0')
        result.append(section)

    # Insert consecutive sections of zeroes
    if consecutive_start > -1:
        inserted_string = '0000:' * (8 - len(sections))
        inserted_string = inserted_string[:len(inserted_string) - 1]
        result.insert(consecutive_start, inserted_string)

    result = ':'.join(result)
    return result

def ipv6_hex2dec_iterative(short_ipv6):
    hex_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    sections = expand_ipv6(short_ipv6).strip().split(':')
    result = ''

    for section in sections:
        decimal = 0
        for i in range(len(section)):
            char = section[i].upper()
            if char in hex_dict:
                char = hex_dict[char]
            else:
                char = int(char)
            decimal += char * 16 ** (len(section) - i - 1)
        result += str(decimal) + ':'

    return result.rstrip(':')

def ipv6_hex2dec(short_ipv6):
    hex_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    long_ipv6_segment = expand_ipv6(short_ipv6).strip()
    result = ''

    colon_index = long_ipv6_segment.find(':')
    if colon_index == -1:
        segment = long_ipv6_segment
    else:
        segment = long_ipv6_segment[:colon_index]

    decimal = 0
    for i in range(len(segment)):
        char = segment[i].upper()
        if char in hex_dict:
            char = hex_dict[char]
        else:
            char = int(char)
        decimal += char * 16 ** (len(segment) - i - 1)
    result += str(decimal)

    if colon_index == -1:
        return result

    return result + ':' + ipv6_hex2dec_rec(long_ipv6_segment[colon_index + 1:])

def main():
    with open('IPV6_LONG.txt') as long_file:
        with open('IPV6_SHORT.txt') as short_file:
            output_fmt = '{:<40}\t{:<35}\t{:<35}\t{:<10}'
            print(output_fmt.format('Expanded', 'Abbreviated', 'Decimal', 'Matches'))

            for line in long_file:
                long_line = line.strip()
                short_line = short_file.readline().strip()

                abbreviated = abbreviate_ipv6(long_line)
                expanded = expand_ipv6(short_line)
                decimal = ipv6_hex2dec(short_line)

                print(output_fmt.format(expanded, abbreviated, decimal,
                    long_line == expanded and abbreviated == short_line))

main()
