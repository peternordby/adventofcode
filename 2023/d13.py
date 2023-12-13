import re

import numpy as np
from utils import fetch_input


def read_input(TEST=0):
    filename = f"{__file__.split('.')[0]}{['', 'x1', 'x2'][TEST]}.txt"
    with open(filename) as f:
        puzzle = f.read().split('\n\n')
    return puzzle

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


def part1(puzzle):
    t = 0
    for pattern in puzzle:
        pattern = pattern.split('\n')
        for row in range(len(pattern)):
            if check_symmetric(pattern, y=row):
                print(f'Row {row} is symmetric')
                t += row * 100
        for col in range(len(pattern[0])):
            if check_symmetric(pattern, x=col):
                print(f'Col {col} is symmetric')
                t += col
    return t


def part2(puzzle):
    pass

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        TEST = 0
        puzzle = read_input(TEST)
        print(f'Part 1: {part1(puzzle)}')
        print(f'Part 2: {part2(puzzle)}')