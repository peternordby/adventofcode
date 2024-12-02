import re
import sys

import numpy as np
from utils import fetch_input, read_input


def part1(parsed):
    safe = 0
    for report in parsed:
        levels = [int(l) for l in report.split()]
        diffs = [(b - a) for a, b in zip(levels[:-1], levels[1:])]
        if (min(diffs) >= -3 and max(diffs) <= -1) or (min(diffs) >= 1 and max(diffs) <= 3):
            safe += 1

    return safe
        

def part2(parsed):
    safe = 0
    for report in parsed:
        levels = [int(l) for l in report.split()]
        for i, _ in enumerate(levels):
            levels_removed = levels.copy()
            levels_removed.pop(i)
            diffs = [(b - a) for a, b in zip(levels_removed[:-1], levels_removed[1:])]
            if (min(diffs) >= -3 and max(diffs) <= -1) or (min(diffs) >= 1 and max(diffs) <= 3):
                safe += 1
                break

    return safe

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        parsed = content.splitlines()
        print(f'Part 1: {part1(parsed)}')
        print(f'Part 2: {part2(parsed)}')