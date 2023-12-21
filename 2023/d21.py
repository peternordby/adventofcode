import re
import sys
from functools import cache

import numpy as np
from utils import fetch_input, read_input


@cache
def get_nbrs(pos):
    global grid
    global garden_spots
    nbrs = []
    nbrs_pos = [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]
    for nbr_pos in nbrs_pos:
        if 0 <= nbr_pos[0] < len(grid) and 0 <= nbr_pos[1] < len(grid[0]) and grid[nbr_pos[0]][nbr_pos[1]] != '#':
            if nbr_pos not in garden_spots:
                nbrs.append(nbr_pos)

    return nbrs

@cache
def dfs(pos, step, step_goal):
    global garden_spots

    if step == step_goal:
        garden_spots.add(pos)
        return
    
    nbrs = get_nbrs(pos)
    for nbr in nbrs:
        dfs(nbr, step + 1, step_goal)


grid = None
garden_spots = set()

def part1(parsed):
    global grid
    grid = parsed
    step_goal = 64

    for r, row in enumerate(parsed):
        for c, char in enumerate(row):
            if char == 'S':
                dfs((r, c), 0, step_goal)

    return len(garden_spots)

def part2(parsed):
    # Hitting recursion depth limit
    # Bruteforce does not end in reasonable time with cache
    # Can't find the smart solution :(
    pass  

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        parsed = [[char for char in row] for row in content.splitlines()]
        print(f'Part 1: {part1(parsed)}')
        print(f'Part 2: {part2(parsed)}')