import re
import sys
from functools import cache

import numpy as np
from utils import fetch_input, read_input


def get_nbrs(grid, pos, path):
    nbrs = []
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    if grid[pos[0]][pos[1]] == '<':
        if tuple(np.add(pos, dirs[0])) not in path:
            nbrs.append(tuple(np.add(pos, dirs[0])))
    elif grid[pos[0]][pos[1]] == '>':
        if tuple(np.add(pos, dirs[1])) not in path:
            nbrs.append(tuple(np.add(pos, dirs[1])))
    elif grid[pos[0]][pos[1]] == '^':
        if tuple(np.add(pos, dirs[2])) not in path:
            nbrs.append(tuple(np.add(pos, dirs[2])))
    elif grid[pos[0]][pos[1]] == 'v':
        if tuple(np.add(pos, dirs[3])) not in path:
            nbrs.append(tuple(np.add(pos, dirs[3])))
    else:
        for d in dirs:
            nbr_pos = tuple(np.add(pos, d))
            if 0 <= nbr_pos[0] < len(grid) and 0 <= nbr_pos[1] < len(grid[0]) and grid[nbr_pos[0]][nbr_pos[1]] != '#' and nbr_pos not in path:
                nbrs.append(nbr_pos)
    return nbrs

def get_longest_path(grid, pos, end, path):
    path.append(pos)
    nbrs = get_nbrs(grid, pos, path)
    if not nbrs:
        return 0
    longest = 0
    for nbr in nbrs:
        if nbr == end:
            return 1
        char = grid[nbr[0]][nbr[1]]
        if char != '#':
            sub_longest = get_longest_path(grid, nbr, end, path.copy())
            longest = max(longest, sub_longest)
    return 1 + longest

def part1(parsed):
    start = (0, parsed[0].index('.'))
    end = (len(parsed) - 1, parsed[-1].index('.'))
    sys.setrecursionlimit(10000)
    
    return get_longest_path(parsed, start, end, [])
    

def part2(parsed):
    pass

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        parsed = [[ch for ch in row] for row in content.splitlines()]
        print(f'Part 1: {part1(parsed)}')
        print(f'Part 2: {part2(parsed)}')