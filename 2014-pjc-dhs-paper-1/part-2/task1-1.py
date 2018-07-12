#!/usr/bin/env python3

def main():
    fastest_runner_id = None
    fastest_chip_time = 1e9

    file = open('RACE.txt')
    for line in file:
        line = line.strip()
        runner_id = line[:5]
        start_hr, start_min, start_sec = [int(line[5:7]), int(line[8:10]), int(line[11:13])]
        end_hr, end_min, end_sec = [int(line[13:15]), int(line[16:18]), int(line[19:])]
        start_time = start_hr * 3600 + start_min * 60 + start_sec # seconds
        end_time = end_hr * 3600 + end_min * 60 + end_sec # seconds
        chip_time = end_time - start_time
        if chip_time < fastest_chip_time:
            fastest_chip_time = chip_time
            fastest_runner_id = runner_id
    file.close()

    fastest_chip_hr = fastest_chip_time // 3600
    fastest_chip_min = (fastest_chip_time % 3600) // 60
    fastest_chip_sec = (fastest_chip_time % 3600) % 60
    print('Fastest runner id:', fastest_runner_id, '\tChip time:',
        fastest_chip_hr, 'h', fastest_chip_min, 'm', fastest_chip_sec, 's')

main()
