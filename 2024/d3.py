import re
import sys

import numpy as np
from utils import fetch_input, read_input


def part1(parsed):
    ans = 0
    matches = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", parsed)
    for match in matches:
        a, b = match[4:-1].split(",")
        ans += int(a) * int(b)

    return ans

def part2(parsed):
    ans = 0
    matches = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)|don't\(\)|do\(\)", parsed)
    multiply = True
    for match in matches:
        if match == "don't()":
            multiply = False
        elif match == "do()":
            multiply = True
        else:
            if multiply:
                a, b = match[4:-1].split(",")
                ans += int(a) * int(b)

    return ans

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        print(f'Part 1: {part1(content)}')
        print(f'Part 2: {part2(content)}')