import re
import sys

import numpy as np
from utils import fetch_input, read_input


def check_symmetric(pattern, x=None, y=None):
    # Check vertical line
    if x:
        # x is first row to the right of the vertical line
        for row in pattern:
            # Reverse left
            left = row[:x][::-1]
            right = row[x:]
            for l, r in zip(left, right):
                if l != r:
                    return False
        return True

    # Check horizontal line
    if y:
        # Rotate pattern 90 degrees using np
        pattern = [[ch for ch in row] for row in pattern]
        rot = np.array(pattern).T.tolist()

        for row in rot:
            # Reverse left
            left = row[:y][::-1]
            right = row[y:]
            for l, r in zip(left, right):
                if l != r:
                    return False
        return True


def part1(parsed):
    t = 0
    for pattern in parsed:
        pattern = pattern.split('\n')
        for row in range(len(pattern)):
            if check_symmetric(pattern, y=row):
                t += row * 100
        for col in range(len(pattern[0])):
            if check_symmetric(pattern, x=col):
                t += col
    return t


def part2(parsed):
    pass

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        parsed = content.split('\n\n')
        print(f'Part 1: {part1(parsed)}')
        print(f'Part 2: {part2(parsed)}')