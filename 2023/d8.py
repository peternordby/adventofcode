import re
import sys

from utils import fetch_input, read_input


def part1(parsed):
    dirs = parsed[0].strip()

    mapping = {}

    for line in parsed[2:]:
        line = line.strip()
        pos, nexts = line.split('=')
        pos = pos.strip()
        l, r = nexts.split(',')
        l = l.strip().replace('(', '')
        r = r.strip().replace(')', '')
        mapping[pos] = (l, r)

    pos = 'AAA'
    steps = 0
    while True:
        d = dirs[steps % len(dirs)]
        if d == 'R':
            pos = mapping[pos][1]
        elif d == 'L':
            pos = mapping[pos][0]
        steps += 1
        if pos == 'ZZZ':
            return steps

def part2(parsed):
    dirs = parsed[0].strip()

    mapping = {}

    for line in parsed[2:]:
        line = line.strip()
        pos, nexts = line.split('=')
        pos = pos.strip()
        l, r = nexts.split(',')
        l = l.strip().replace('(', '')
        r = r.strip().replace(')', '')
        mapping[pos] = (l, r)

    ends_with_A = [k for k in mapping.keys() if k[2] == 'A']
    ends_with_Z = [k for k in mapping.keys() if k[2] == 'Z']

    steps = 0
    all_steps = []
    pos = ends_with_A
    curr_steps = []

    for p in pos:
        while True:
            d = dirs[steps % len(dirs)]
            if d == 'R':
                p = mapping[p][1]
            elif d == 'L':
                p = mapping[p][0]
            steps += 1
            if p in ends_with_Z:
                curr_steps.append(steps)
                if len(curr_steps) == 2:
                    # print differences between steps
                    all_steps.append(curr_steps)
                    curr_steps = []
                    break

    from math import lcm
    return lcm(*[step[1]-step[0] for step in all_steps])
    

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        parsed = content.splitlines()
        print(f'Part 1: {part1(parsed)}')
        print(f'Part 2: {part2(parsed)}')