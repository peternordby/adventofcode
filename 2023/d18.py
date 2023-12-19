import re
import sys

import numpy as np
from shapely.geometry import Polygon
from utils import fetch_input, read_input


def part1(parsed):
    start = (0, 0)
    dug = set()

    dirs = {
        'R': [0, 1],
        'U': [-1, 0],
        'L': [0, -1],
        'D': [1, 0],
    }

    pos = start
    for line in parsed:
        d, l, c = line.split()

        for _ in range(int(l)):
            pos = tuple(np.add(pos, dirs[d]))
            dug.add((pos, c.strip('(').strip(')')))

    min_row = min(dug, key=lambda x: x[0][0])[0][0]
    min_col = min(dug, key=lambda x: x[0][1])[0][1]

    # Adjust all coordinates to be positive
    dug = set(((x - min_row, y - min_col), c) for (x, y), c in dug)

    # Find the dimensions of the grid
    rows = max(dug, key=lambda x: x[0][0])[0][0] + 1
    cols = max(dug, key=lambda x: x[0][1])[0][1] + 1

    grid = np.zeros((rows, cols))

    # Set the dug coordinates to 1
    for (x, y), c in dug:
        grid[x, y] = 1

    # Find all coordinates that are not dug
    not_dug = set()
    for i in range(rows):
        for j in range(cols):
            if grid[i, j] == 0:
                not_dug.add((i, j))

    # Find the interior of the dug area
    while not_dug:
        # Pick a random starting point
        # Flood fill from that point (BFS)
        # If the flood touches the border of the grid,
        # it is not the interior of the dug area, so remove it from the set
        flood = set()
        while True:
            start = not_dug.pop()
            flood.add(start)
            stack = [start]
            while stack:
                x, y = stack.pop()
                for dx, dy in dirs.values():
                    if (x + dx, y + dy) in not_dug and (x + dx, y + dy) not in flood:
                        flood.add((x + dx, y + dy))
                        stack.append((x + dx, y + dy))
            break

        # Check if flood touches border of grid
        if any(x == 0 or y == 0 or x == rows - 1 or y == cols - 1 for x, y in flood):
            not_dug -= flood
        else:
            break

    # Set the interior of the dug area to 2
    for x, y in flood:
        grid[x, y] = 2

    # Find the area of the dug area including the interior
    area = np.sum(grid == 1) + np.sum(grid == 2)

    return area


def part2(parsed):
    dirs = {
        'R': [0, 1],
        'U': [-1, 0],
        'L': [0, -1],
        'D': [1, 0],
    }

    start = (0, 0)
    polygon = [start]
    for line in parsed:
        d, l, c = line.split()
        c = c.strip('(').strip(')')
        l = int(c[1:-1], 16)
        d = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}[int(c[-1], 16)]

        polygon.append(tuple(np.add(polygon[-1], np.multiply(dirs[d], l))))

    interior = Polygon(polygon).area
    border = int(Polygon(polygon).exterior.length)
    area = int(interior + border/2 + 1)
    return area

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        parsed = content.splitlines()
        print(f'Part 1: {part1(parsed)}')
        print(f'Part 2: {part2(parsed)}')