import re
import sys

import numpy as np
from utils import fetch_input, read_input


def part1(parsed):
    ans = 0

    for i, line in enumerate(parsed):
        for j, char in enumerate(line):
            if char == "X":
                target = "XMAS"
            elif char == "S":
                target = "SAMX"
            else:
                continue

            try:
                forward = parsed[i][j] + parsed[i][j+1] + parsed[i][j+2] + parsed[i][j+3]
            except:
                forward = None
            try:
                down = parsed[i][j] + parsed[i+1][j] + parsed[i+2][j] + parsed[i+3][j]
            except:
                down = None
            try:
                diagonal_right = parsed[i][j] + parsed[i+1][j+1] + parsed[i+2][j+2] + parsed[i+3][j+3]
            except:
                diagonal_right = None
            try:
                if j-3 < 0:
                    raise IndexError
                diagonal_left = parsed[i][j] + parsed[i+1][j-1] + parsed[i+2][j-2] + parsed[i+3][j-3]
            except:
                diagonal_left = None

            directions = [forward, down, diagonal_right, diagonal_left]
            for word in directions:
                if word == target:
                    ans += 1

    return ans


def part2(parsed):
    ans = 0

    for i, line in enumerate(parsed):
        for j, char in enumerate(line):
            if not char == "A":
                continue

            try:
                if j-1 < 0 or i-1 < 0:
                    raise IndexError
                diagonal_right = parsed[i-1][j-1] + parsed[i][j] + parsed[i+1][j+1]
            except:
                diagonal_right = None
            try:
                if j-1 < 0 or i-1 < 0:
                    raise IndexError
                diagonal_left = parsed[i-1][j+1] + parsed[i][j] + parsed[i+1][j-1]
            except:
                diagonal_left = None

            if diagonal_left in ("MAS", "SAM") and diagonal_right in ("MAS", "SAM"):
                ans += 1

    return ans

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        parsed = content.splitlines()
        print(f'Part 1: {part1(parsed)}')
        print(f'Part 2: {part2(parsed)}')