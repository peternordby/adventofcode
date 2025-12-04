import re
import sys

from utils import fetch_input, read_input


def part1(parsed):
    ans = 0
    for r, line in enumerate(parsed):
        for c, char in enumerate(line):
            if char == "@":
                count = 0
                for y in range(-1, 2):
                    for x in range(-1, 2):
                        if r + y < 0 or c + x < 0:
                            continue
                        if y == 0 and x == 0:
                            continue
                        try:
                            if parsed[r + y][c + x] == "@":
                                count += 1
                        except IndexError:
                            continue
                if count < 4:
                    ans += 1
    return ans


def part2(parsed):
    ans = 0
    while True:
        to_remove = set()
        for r, line in enumerate(parsed):
            for c, char in enumerate(line):
                if char == "@":
                    count = 0
                    for y in range(-1, 2):
                        for x in range(-1, 2):
                            if r + y < 0 or c + x < 0:
                                continue
                            if y == 0 and x == 0:
                                continue
                            try:
                                if parsed[r + y][c + x] == "@":
                                    count += 1
                            except IndexError:
                                continue
                    if count < 4:
                        to_remove.add((r, c))
                        ans += 1
        if len(to_remove) > 0:
            for r, line in enumerate(parsed):
                for c, char in enumerate(line):
                    if (r, c) in to_remove:
                        parsed[r][c] = "."
        else:
            break
    return ans


if __name__ == "__main__":
    day = int(re.findall(r"\d+", __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ""
        content = read_input(day, in_file)
        parsed = content.splitlines()
        parsed = [[c for c in line] for line in parsed]
        print(f"Part 1: {part1(parsed)}")
        print(f"Part 2: {part2(parsed)}")
