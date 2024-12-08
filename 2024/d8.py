import re
import sys

import numpy as np
from utils import fetch_input, read_input


def part1(parsed):
    R = len(parsed)
    C = len(parsed[0])

    freqs = {}

    for i, line in enumerate(parsed):
        for j, char in enumerate(line):
            if char in freqs:
                freqs[char].append((i, j))
            elif char != ".":
                freqs[char] = [(i,j)]

    anti_nodes = set()
    for freq in freqs.keys():
        for a in freqs[freq]:
            for b in freqs[freq]:
                if a == b:
                    continue

                anti_node = (2 * a[0] - b[0], 2 * a[1] - b[1])

                if 0 <= anti_node[0] < R and 0 <= anti_node[1] < C:
                    anti_nodes.add(anti_node)

    return len(anti_nodes)

def part2(parsed):
    R = len(parsed)
    C = len(parsed[0])

    freqs = {}

    for i, line in enumerate(parsed):
        for j, char in enumerate(line):
            if char in freqs:
                freqs[char].append((i, j))
            elif char != ".":
                freqs[char] = [(i,j)]

    anti_nodes = set()
    for freq in freqs.keys():
        for a in freqs[freq]:
            for b in freqs[freq]:
                if a == b:
                    continue

                for i in range(51):
                    anti_node = (a[0] + (a[0] - b[0]) * i, a[1] + (a[1] - b[1]) * i)

                    if 0 <= anti_node[0] < R and 0 <= anti_node[1] < C:
                        anti_nodes.add(anti_node)

    return len(anti_nodes)

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        parsed = content.splitlines()
        print(f'Part 1: {part1(parsed)}')
        print(f'Part 2: {part2(parsed)}')