import re
import sys

import numpy as np
from utils import fetch_input, read_input


def set_sand(sands, start, end, i):
    for x in range(start[0], end[0] + 1):
        for y in range(start[1], end[1] + 1):
            for z in range(start[2], end[2] + 1):
                sands[x, y, z] = i+1

def make_fall(sands, start, end, i, brick_dict):
    # Make sand fall
    orig_start = start.copy()
    orig_end = end.copy()

    stop = False
    while start[2] > 1 and not stop:
        # Check if resting on another piece of sand
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                if sands[x, y, start[2] - 1] != 0:
                    stop = True
        if not stop:
            start[2] -= 1
            end[2] -= 1

    # Clear original position
    set_sand(sands, orig_start, orig_end, -1)

    # Set new position
    set_sand(sands, start, end, i)
    brick_dict[i+1] = (start, end)

def part1(parsed):
    sands = np.zeros((10, 10, 500), dtype=int)
    bricks = []

    # Parse bricks
    for i, line in enumerate(parsed):
        start, end  = line.split('~')
        start = [int(x) for x in start.split(',')]
        end = [int(x) for x in end.split(',')]
        bricks.append((start, end))

    # Sort bricks by start z
    bricks.sort(key=lambda x: x[0][2])

    brick_dict = {}
    # Get sand in resting position
    for i, brick in enumerate(bricks):
        brick_dict[i+1] = brick
        start, end = brick
        make_fall(sands, start, end, i, brick_dict)

    # Find which bricks can be removed without affecting above bricks
    removable = set()
    for i, brick in brick_dict.items():
        # Find bricks resting on top of this brick
        # If none, then this brick can be removed
        # If there are bricks resting on top, check if they are resting on other bricks
        # If yes for all, then this brick can be removed

        isRemovable = True

        start, end = brick
        resting = []
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                if sands[x, y, start[2] + 1] != 0:
                    if sands[x, y, start[2] + 1] not in resting:
                        resting.append(sands[x, y, start[2] + 1])

        print(resting)
        for r in resting:
            supporting = []
            start, end = brick_dict[r]
            for x in range(start[0], end[0] + 1):
                for y in range(start[1], end[1] + 1):
                    if sands[x, y, start[2] - 1] != 0:
                        if sands[x, y, start[2] - 1] not in supporting:
                            supporting.append(sands[x, y, start[2] - 1])
            if len(supporting) == 1 and supporting[0] == i:
                isRemovable = False
                break

        if isRemovable:
            removable.add(i)

    return len(removable)

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