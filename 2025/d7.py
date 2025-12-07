import re
import sys
from functools import lru_cache

from utils import fetch_input, read_input


def part1(parsed):
    start = parsed[0].find("S")
    beams = set()
    beams.add(start)
    ans = 0
    for row in parsed[1:]:
        new_beams = set()
        for beam in beams:
            if row[beam] == "^":
                ans += 1
                new_beams.add(beam - 1)
                new_beams.add(beam + 1)
            else:
                new_beams.add(beam)
        beams = new_beams

    return ans


def part2(parsed):
    start = parsed[0].find("S")

    @lru_cache
    def beam(row, col):
        if row == len(parsed) - 1:
            return 1
        if parsed[row][col] == "^":
            return beam(row + 1, col - 1) + beam(row + 1, col + 1)
        return beam(row + 1, col)

    return beam(0, start)


if __name__ == "__main__":
    day = int(re.findall(r"\d+", __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ""
        content = read_input(day, in_file)
        parsed = content.splitlines()
        print(f"Part 1: {part1(parsed)}")
        print(f"Part 2: {part2(parsed)}")
