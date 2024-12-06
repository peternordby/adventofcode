import re
import sys

import numpy as np
from utils import fetch_input, read_input


def part1(parsed):
    start = None
    for i, row in enumerate(parsed):
        for j, char in enumerate(row):
            if char in ("^"):
                start = (i, j)

    max_r = len(parsed[0])
    max_c = len(parsed)

    visited = set()

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # up, right, down, left
    direction = 0
    pos = start
    visited.add(pos)
    next_pos = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])

    while 0 <= next_pos[0] < max_r and 0 <= next_pos[1] < max_c:
        next_tile = parsed[next_pos[0]][next_pos[1]]
        if next_tile == "#":
            direction = (direction + 1) % 4
            next_pos = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])
            next_tile = parsed[next_pos[0]][next_pos[1]]
            continue

        pos = next_pos
        visited.add(next_pos)
        next_pos = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])
        

    return len(visited)

def part2(parsed):
    pass

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        parsed = content.splitlines()
        print(f'Part 1: {part1(parsed)}')
        print(f'Part 2: {part2(parsed)}')