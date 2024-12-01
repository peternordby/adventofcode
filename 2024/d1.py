import re
import sys

import numpy as np
from utils import fetch_input, read_input


def part1(parsed):
    return sum([abs(a_num - b_num) for a_num, b_num in zip(a, b)])

def part2(parsed):
    return sum([num * b.count(num) for num in a])

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        parsed = content.splitlines()
        a = sorted([int(line.split()[0]) for line in parsed])
        b = sorted([int(line.split()[1]) for line in parsed])
        print(f'Part 1: {part1(parsed)}')
        print(f'Part 2: {part2(parsed)}')