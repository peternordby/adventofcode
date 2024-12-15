import math
import re
import sys
from functools import cache

import numpy as np
from utils import fetch_input, read_input


def part1(parsed):
    ans = 0
    for lines in parsed:
        a, b, p = lines.splitlines()
        ax, ay = [int(x) for x in re.findall('[0-9]+', a)]
        bx, by = [int(x) for x in re.findall('[0-9]+', b)]
        px, py = [int(x) for x in re.findall('[0-9]+', p)]

        cost = set()
        for i in range(100):
            for j in range(100):
                if (ax*i + bx*j, ay*i + by*j) == (px, py):
                    cost.add(i*3 + j)

        if cost:
            ans += min(cost)
            
    return ans

def part2(parsed):
    ans = 0
    for lines in parsed:
        a, b, p = lines.splitlines()
        ax, ay = [int(x) for x in re.findall('[0-9]+', a)]
        bx, by = [int(x) for x in re.findall('[0-9]+', b)]
        px, py = [int(x) + 10000000000000 for x in re.findall('[0-9]+', p)]

        a = (px*by - py*bx) / (ax*by - ay*bx)
        b = (py*ax - px*ay) / (ax*by - ay*bx)
        if a == int(a) and b == int(b):
            ans += int(3 * a + b)
            
    return ans

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        parsed = content.split('\n\n')
        print(f'Part 1: {part1(parsed)}')
        print(f'Part 2: {part2(parsed)}')