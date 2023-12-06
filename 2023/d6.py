import re

from utils import fetch_input


def read_input(TEST=0):
    filename = f"{__file__.split('.')[0]}{['', 'x1', 'x2'][TEST]}.txt"
    with open(filename) as f:
        puzzle = f.readlines()
    return puzzle

def part1(puzzle):
    times, distances = puzzle[0].split(':')[1].strip(), puzzle[1].split(':')[1].strip()
    times = [int(x) for x in re.findall(r'\d+', times)]
    distances = [int(x) for x in re.findall(r'\d+', distances)]

    ways_to_beat_records = []
    
    for time, distance in zip(times, distances):
        last_race_end = 0
        ways_to_beat_record = 0
        speed = 0
        for i in range(last_race_end, time+1):
            speed = i
            remaining_time = time - i
            if speed * remaining_time > distance:
                ways_to_beat_record += 1
        ways_to_beat_records.append(ways_to_beat_record)

    product = 1
    for x in ways_to_beat_records:
        product *= x
    return product


def part2(puzzle):
    times, distances = puzzle[0].split(':')[1].strip(), puzzle[1].split(':')[1].strip()
    time = int(times.replace(' ', ''))
    distance = int(distances.replace(' ', ''))
    
    last_race_end = 0
    ways_to_beat_record = 0
    speed = 0
    for i in range(last_race_end, time+1):
        speed = i
        remaining_time = time - i
        if speed * remaining_time > distance:
            ways_to_beat_record += 1

    return ways_to_beat_record

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        TEST = 0
        puzzle = read_input(TEST)
        print(f'Part 1: {part1(puzzle)}')
        print(f'Part 2: {part2(puzzle)}')