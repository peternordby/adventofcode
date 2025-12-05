import re
import sys

from utils import fetch_input, read_input


def part1(parsed):
    ans = 0
    fresh_range, ingredients = parsed
    fresh_range = fresh_range.splitlines()
    ingredients = ingredients.splitlines()

    for ingredient in ingredients:
        for fresh in fresh_range:
            a, b = fresh.split("-")
            a, b = int(a), int(b)
            ingredient = int(ingredient)
            if a <= ingredient <= b:
                ans += 1
                break

    return ans


def part2(parsed):
    fresh_range, _ = parsed
    fresh_range = fresh_range.splitlines()

    ranges = [
        (
            int(r.split("-")[0]),
            int(r.split("-")[1]),
        )
        for r in fresh_range
    ]

    loops = 0
    while True:
        loops += 1
        new_ranges = []
        for r in ranges:
            a, b = r
            extended = False
            discard = False
            for other in ranges:
                ra, rb = other
                if (a, b) == (ra, rb):
                    continue
                if ra <= a <= rb:
                    if rb < b:
                        new_ranges.append((ra, b))
                        extended = True
                    else:
                        discard = True
                elif ra <= b <= rb:
                    if a < ra:
                        new_ranges.append((a, rb))
                        extended = True
                    else:
                        discard = True
            if not extended and not discard:
                new_ranges.append((a, b))
        new_ranges = list(set(new_ranges))
        if set(ranges) == set(new_ranges):
            break
        ranges = new_ranges

    ans = 0
    for r in ranges:
        a, b = r
        ans += b + 1 - a

    return ans


if __name__ == "__main__":
    day = int(re.findall(r"\d+", __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ""
        content = read_input(day, in_file)
        parsed = content.split("\n\n")
        print(f"Part 1: {part1(parsed)}")
        print(f"Part 2: {part2(parsed)}")
