import re
import sys
from copy import deepcopy

import numpy as np
from utils import fetch_input, read_input


def move(pos, d: str, R, C):
    match d:
        case "UP":
            r = pos[0] - 1
            c = pos[1]
        case "RIGHT":
            r = pos[0]
            c = pos[1] + 1
        case "DOWN":
            r = pos[0] + 1
            c = pos[1]
        case "LEFT": 
            r = pos[0]
            c = pos[1] - 1

    if 0 <= r < R and 0 <= c < C:
        return (r, c)
    
    return None

def count_trails(trailmap, tops, height, pos, R, C):
    if height == 9:
        tops.add(pos)
        return

    for d in ["UP", "RIGHT", "DOWN", "LEFT"]:
        new_pos = move(pos, d, R, C)
        if new_pos and trailmap[new_pos[0]][new_pos[1]] == height + 1:
            count_trails(trailmap, tops, height + 1, new_pos, R, C)

    return len(tops)

def count_trails2(trailmap, height, pos, R, C):
    if height == 0:
        return 1
    
    count = 0

    for d in ["UP", "RIGHT", "DOWN", "LEFT"]:
        new_pos = move(pos, d, R, C)
        if new_pos and trailmap[new_pos[0]][new_pos[1]] == height - 1:
            count += count_trails2(trailmap, height - 1, new_pos, R, C)

    return count

def part1(parsed):
    trailmap = [[int(x) for x in row] for row in parsed]
    R = len(trailmap)
    C = len(trailmap[0])

    ans = 0
    for i, row in enumerate(trailmap):
        for j, height in enumerate(row):
            if height == 0:
                tops = set()
                trails = count_trails(trailmap, tops, 0, (i, j), R, C)
                ans += trails

    return ans

def part2(parsed):
    trailmap = [[int(x) for x in row] for row in parsed]
    R = len(trailmap)
    C = len(trailmap[0])

    ans = 0
    for i, row in enumerate(trailmap):
        for j, height in enumerate(row):
            if height == 9:
                trails = count_trails2(trailmap, 9, (i, j), R, C)
                ans += trails

    return ans

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        parsed = content.splitlines()
        print(f'Part 1: {part1(parsed)}')
        print(f'Part 2: {part2(parsed)}')