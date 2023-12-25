import re
import sys

import numpy as np
import z3
from shapely.geometry import LineString, Point
from utils import fetch_input, read_input


def line_interection(line1, line2, lower, upper):
    p1, v1 = line1
    p2, v2 = line2

    px1, py1 = p1
    px2, py2 = p2
    vx1, vy1 = v1
    vx2, vy2 = v2

    s1 = vy1 / vx1
    s2 = vy2 / vx2

    if s1 == s2:
        return None 
    
    x, y = np.linalg.solve([[-s1, 1], [-s2, 1]], [py1 - s1 * px1, py2 - s2 * px2])
    if (x - px1) / vx1 < 0 or (x - px2) / vx2 < 0:
        return None
    
    if lower < x < upper and lower < y < upper:
        return x, y
    
    return None


def part1(parsed):
    ps = []
    vs = []
    for line in parsed:
        p, v = line.split('@')
        p = tuple([int(x) for x in p.split(',')][:2])
        v = tuple([int(x) for x in v.split(',')][:2])
        ps.append(p)
        vs.append(v)

    test_lower = 7
    test_upper = 27

    real_lower = 200000000000000
    real_upper = 400000000000000

    intersections = []
    for a, line in enumerate(zip(ps, vs)):
        for other in zip(ps[a+1:], vs[a+1:]):
            intersection = line_interection(line, other, real_lower, real_upper)
            if intersection: intersections.append(intersection)

    return len(intersections)

def part2(parsed):
    pass

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        parsed = content.splitlines()
        print(f'Part 1: {part1(parsed)}')
        print(f'Part 2: {part2(parsed)}')