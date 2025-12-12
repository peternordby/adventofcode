import re
import sys

from shapely.geometry import Polygon
from utils import fetch_input, read_input


def area(a, b):
    x = abs(a[0] - b[0]) + 1
    y = abs(a[1] - b[1]) + 1
    return x * y


def part1(parsed):
    coords = [(int(x.split(",")[0]), int(x.split(",")[1])) for x in parsed]
    areas = [
        area(this, other) for i, this in enumerate(coords) for other in coords[i + 1 :]
    ]
    return sorted(areas).pop()


def part2(parsed):
    coords = [(int(x.split(",")[0]), int(x.split(",")[1])) for x in parsed]
    polygon = Polygon(coords)
    areas = []
    for i, this in enumerate(coords):
        for other in coords[i + 1 :]:
            x_min = min(this[0], other[0])
            x_max = max(this[0], other[0])
            y_min = min(this[1], other[1])
            y_max = max(this[1], other[1])
            rect = Polygon(
                [(x_min, y_min), (x_min, y_max), (x_max, y_max), (x_max, y_min)]
            )
            if polygon.contains(rect):
                areas.append(area(this, other))
    return sorted(areas).pop()


if __name__ == "__main__":
    day = int(re.findall(r"\d+", __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ""
        content = read_input(day, in_file)
        parsed = content.splitlines()
        print(f"Part 1: {part1(parsed)}")
        print(f"Part 2: {part2(parsed)}")
