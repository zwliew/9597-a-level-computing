#!/usr/bin/env python3

def main():
    runners = []

    file = open('RACE.txt')
    for line in file:
        line = line.strip()
        runner_id = line[:5]
        start_hr, start_min, start_sec = [int(line[5:7]), int(line[8:10]), int(line[11:13])]
        end_hr, end_min, end_sec = [int(line[13:15]), int(line[16:18]), int(line[19:])]
        start_time = start_hr * 3600 + start_min * 60 + start_sec # seconds
        end_time = end_hr * 3600 + end_min * 60 + end_sec # seconds
        chip_time = end_time - start_time
        runners.append([runner_id, chip_time])
    file.close()

    for i in range(1, len(runners)):
        cur = runners[i]
        j = i - 1
        while j >= 0 and runners[j][1] > cur[1]:
            runners[j + 1] = runners[j]
            j -= 1
        runners[j + 1] = cur

    count = 0
    rank = 0
    prev_time = 1e9
    while rank < 4:
        runner_id, chip_time = runners[count]
        if prev_time != chip_time:
            prev_time = chip_time
            rank += 1
        if rank < 4:
            chip_hr = prev_time // 3600
            chip_min = (prev_time % 3600) // 60
            chip_sec = (prev_time % 3600) % 60
            print('{:<1}. {:<5}\tChip time: {:<2} h {:<2} m {:<2} s'
                .format(rank, runner_id, chip_hr, chip_min, chip_sec))
        count += 1

main()
