import re
import sys

from utils import fetch_input, read_input


def part1(parsed):
    times, distances = parsed[0].split(':')[1].strip(), parsed[1].split(':')[1].strip()
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


def part2(parsed):
    times, distances = parsed[0].split(':')[1].strip(), parsed[1].split(':')[1].strip()
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
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        parsed = content.splitlines()
        print(f'Part 1: {part1(parsed)}')
        print(f'Part 2: {part2(parsed)}')