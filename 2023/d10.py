import re
import sys

from utils import fetch_input, read_input

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

def bfs(grid, start):
    visited = set()
    loop = [(start, 0)]
    depth = 0
    queue = [(start, depth)]
    while queue:
        pos, depth = queue.pop(0)
        visited.add(pos)
        pipe = grid[pos[0]][pos[1]]
        for nbr_dir in pipe2nb[pipe]:
            nbr = dirs[nbr_dir]
            nbr_row, nbr_col = pos[0] + nbr[0], pos[1] + nbr[1]
            nbp = grid[nbr_row][nbr_col]
            opp_dir =  (nbr[0]*-1, nbr[1]*-1)
            if opp_dir in [dirs[d] for d in pipe2nb[nbp]]:
                if (nbr_row, nbr_col) not in visited:
                    queue.append(((nbr_row, nbr_col), depth + 1))
                    visited.add((nbr_row, nbr_col))
                    loop.append(((nbr_row, nbr_col), depth + 1))
    return loop

def part1(parsed):
    for row, line in enumerate(parsed):
        for col, char in enumerate(line):
            if char == 'S':
                start = (row, col)  
    loop = bfs(parsed, start) 
    depths = [pipe[1] for pipe in loop]

    return max(depths)

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