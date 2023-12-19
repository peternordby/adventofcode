import heapq
import re
import sys

import numpy as np
from utils import fetch_input, read_input

dirs = {
    'U': (-1, 0),
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1),
}

def dijkstra(grid, start, end, min_steps=0, max_steps=3):
    queue = []
    heat_loss = 0
    curr = start
    d = None
    steps = 0

    heapq.heappush(queue, (heat_loss, curr, d, steps))

    seen = set()

    while queue:
        heat_loss, curr, d, steps = heapq.heappop(queue)
        
        if curr == end:
            return heat_loss
        
        if (curr, d, steps) in seen:
            continue

        seen.add((curr, d, steps))

        nexts = []

        if d is None:
            nexts = [(tuple(np.add(curr, dirs[d])), d, 1) for d in dirs.keys()]

        else:
            if d in 'LR' and min_steps <= steps:
                [nexts.append((tuple(np.add(curr, dirs[d])), d, 1)) for d in 'UD']
            elif d in 'UD' and min_steps <= steps:
                [nexts.append((tuple(np.add(curr, dirs[d])), d, 1)) for d in 'LR']

            if steps < max_steps:
                nexts.append((tuple(np.add(curr, dirs[d])), d, steps + 1))

        for nxt, d, steps in nexts:
            if (0 <= nxt[0] < len(grid)) and (0 <= nxt[1] < len(grid[0])):
                new_heat_loss = heat_loss + grid[nxt[0]][nxt[1]]
                heapq.heappush(queue, (new_heat_loss, nxt, d, steps))


def part1(parsed):
    grid = np.array(parsed)
    start = (0, 0)
    rows, cols = grid.shape
    end = (rows - 1, cols - 1)
    return dijkstra(grid, start, end)

def part2(parsed):
    grid = np.array(parsed)
    start = (0, 0)
    rows, cols = grid.shape
    end = (rows - 1, cols - 1)
    return dijkstra(grid, start, end, min_steps=4, max_steps=10)

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        parsed = [[int(x) for x in row] for row in content.splitlines()]
        print(f'Part 1: {part1(parsed)}')
        print(f'Part 2: {part2(parsed)}')