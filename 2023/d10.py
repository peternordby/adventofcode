import re

from utils import fetch_input


def read_input(TEST=0):
    filename = f"{__file__.split('.')[0]}{['', 'x1', 'x2'][TEST]}.txt"
    with open(filename) as f:
        puzzle = [[ch for ch in row.strip()] for row in f.readlines()]
    return puzzle

dirs = {
    'N': (-1, 0),
    'S': (1, 0),
    'E': (0, 1),
    'W': (0, -1),
}

pipe2nb = {
    '|': ['N', 'S'],            # | is a vertical pipe connecting north and south.
    '-': ['E', 'W'],            # - is a horizontal pipe connecting east and west.
    'L': ['N', 'E'],            # L is a 90-degree bend connecting north and east.
    'J': ['N', 'W'],            # J is a 90-degree bend connecting north and west.
    '7': ['S', 'W'],            # 7 is a 90-degree bend connecting south and west.
    'F': ['S', 'E'],            # F is a 90-degree bend connecting south and east.
    '.': [None],                # . is ground; there is no pipe in this tile.
    'S': ['N', 'S', 'E', 'W'],  # S is the starting position of the animal
}

char2pipe = {
    '|': '│',
    '-': '─',
    '7': '┐',
    'J': '┘',
    'F': '┌',
    'L': '└',
    'S': '█',
}

def bfs(puzzle, start):
    visited = set()
    loop = [(start, 0)]
    depth = 0
    queue = [(start, depth)]
    while queue:
        pos, depth = queue.pop(0)
        visited.add(pos)
        pipe = puzzle[pos[0]][pos[1]]
        for nbr_dir in pipe2nb[pipe]:
            nbr = dirs[nbr_dir]
            nbr_row, nbr_col = pos[0] + nbr[0], pos[1] + nbr[1]
            nbp = puzzle[nbr_row][nbr_col]
            opp_dir =  (nbr[0]*-1, nbr[1]*-1)
            if opp_dir in [dirs[d] for d in pipe2nb[nbp]]:
                if (nbr_row, nbr_col) not in visited:
                    queue.append(((nbr_row, nbr_col), depth + 1))
                    visited.add((nbr_row, nbr_col))
                    loop.append(((nbr_row, nbr_col), depth + 1))
    return loop

def part1(puzzle):
    for row, line in enumerate(puzzle):
        for col, char in enumerate(line):
            if char == 'S':
                start = (row, col)  
    print(start)
    loop = bfs(puzzle, start) 
    pipes = [pipe[0] for pipe in loop]
    depths = [pipe[1] for pipe in loop]

    for row, line in enumerate(puzzle):
        for col, char in enumerate(line):
            if (row, col) in pipes:
                print(char2pipe[puzzle[row][col]], end='')
            else:
                print(' ', end='')
        print()

    return pipes, max(depths)

def part2(puzzle, pipes):
    pass

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        TEST = 0
        puzzle = read_input(TEST)
        pipes, depth = part1(puzzle)
        print(f'Part 1: {depth}')
        print(f'Part 2: {part2(puzzle, pipes)}')