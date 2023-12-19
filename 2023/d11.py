import re
import sys

import numpy as np
from utils import fetch_input, read_input


def expand(universe: list[list[str]], p2 = False):
    nu = []
    for row in universe:
        if all([x == '.' for x in row]):
            nu.append(row if not p2 else ['R'] * len(row))
            if not p2:
                nu.append(row)
        else:
            nu.append(row)

    universe = np.array(nu).T
    nu = []
    for col in universe:
        if all([x != '#' for x in col]):
            nu.append(col if not p2 else ['C'] * len(col))
            if not p2:
                nu.append(col)
        else:
            nu.append(col)
    return np.array(nu).T.tolist()

def manhattan_distance(p1: tuple, p2: tuple):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def smart_distance(universe, p1: tuple, p2: tuple, mult):
    st_row = min(p1[0], p2[0])
    en_row = max(p1[0], p2[0])
    st_col = min(p1[1], p2[1])
    en_col = max(p1[1], p2[1])

    rc, cc = 0, 0

    if st_row != en_row:
        c = [r[0] for r in universe][st_row:en_row+1]
        rc = c.count('R')

    if st_col != en_col:
        r = universe[0][st_col:en_col+1]
        cc = r.count('C')

    dist = manhattan_distance(p1, p2) + cc * mult + rc * mult - cc - rc

    return dist

def part1(parsed):
    expanded = expand(parsed)

    indexes = []
    for i in range(len(expanded)):
        for j in range(len(expanded[i])):
            if expanded[i][j] == '#':
                indexes.append((i, j))

    pairs = []
    for i in range(len(indexes)):
        for j in range(i, len(indexes)):
            if i != j:
                pairs.append((indexes[i], indexes[j]))

    t = 0
    for pair in pairs:
        t += manhattan_distance(pair[0], pair[1])

    return t

def part2(parsed):
    expanded = expand(parsed, p2=True)

    indexes = []
    for i in range(len(expanded)):
        for j in range(len(expanded[i])):
            if expanded[i][j] == '#':
                indexes.append((i, j))

    pairs = []
    for i in range(len(indexes)):
        for j in range(i, len(indexes)):
            if i != j:
                pairs.append((indexes[i], indexes[j]))

    t = 0
    for pair in pairs:
        t += smart_distance(expanded, pair[0], pair[1], mult=1_000_000)

    return t

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        parsed = [[ch for ch in row] for row in content.splitlines()]
        print(f'Part 1: {part1(parsed)}')
        print(f'Part 2: {part2(parsed)}')