import re

import numpy as np
from utils import fetch_input


def read_input(TEST=0):
    filename = f"{__file__.split('.')[0]}{['', 'x1', 'x2'][TEST]}.txt"
    with open(filename) as f:
        puzzle = [[ch for ch in row] for row in f.read().splitlines()]
    return puzzle

def move_rocks(grid):
    for i, row in enumerate(grid):
        string = ''.join(row)
        segments = string.split('#')
        new_segments = []
        for segment in segments:
            o_count = segment.count('O')
            ns = "".join(['O' * o_count, '.' * (len(segment) - o_count)])
            new_segments.append(ns)
        new_string = '#'.join(new_segments)
        grid[i] = list(new_string)
    return grid

def tilt(puzzle, direction):
    grid = np.array(puzzle)
    match direction:
        case 'N':
            rot = np.rot90(grid, 1)
            grid = move_rocks(rot)
            grid = np.rot90(grid, 3)

        case 'W':
            grid = move_rocks(grid)

        case 'S':
            rot = np.rot90(grid, 3)
            grid = move_rocks(rot)
            grid = np.rot90(grid, 1)

        case 'E':
            rot = np.rot90(grid, 2)
            grid = move_rocks(rot)
            grid = np.rot90(grid, 2)
    
    return grid.tolist()
        
def calc_load(puzzle):
    rot = np.array(puzzle).T.tolist()
    load = 0

    for row in rot:
        rev = row[::-1]
        for i, ch in enumerate(rev):
            if ch == 'O':
                load += i+1

    return load


def cycle(grid):
    dirs = ['N', 'W', 'S', 'E']
    for direction in dirs:
        grid = tilt(grid.copy(), direction)
    return grid

def part1(puzzle):
    tilted = tilt(puzzle, 'N')
    load = calc_load(tilted)
    return load

def part2(puzzle):
    max_cycles = 1_000_000_000
    grid_cache = {}

    for i in range(max_cycles):
        puzzle = cycle(puzzle)

        print(f'Done with cycle {i+1}')

        grid_tuple = tuple(tuple(row) for row in puzzle)

        if grid_tuple in grid_cache:
            repeat_length = i - grid_cache[grid_tuple]
            print(f'Found repeat at cycle {i+1} with length {repeat_length}')
            break

        grid_cache[grid_tuple] = i

    for _ in range((max_cycles - (i + 1)) % repeat_length):
        puzzle = cycle(puzzle)

    load = calc_load(puzzle)
    return load

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        TEST = 0
        puzzle = read_input(TEST)
        print(f'Part 1: {part1(puzzle)}')
        print(f'Part 2: {part2(puzzle)}')