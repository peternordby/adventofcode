import re
import sys

from utils import fetch_input, read_input


def part1(parsed):
    dial = 50
    count = 0

    for line in parsed:
        direction, amount = line[0], int(line[1:])
        dial = dial - amount if direction == "L" else dial + amount
        dial = dial % 100
        count = count + 1 if dial == 0 else count

    return count


def part2(parsed):
    dial = 50
    count = 0

    for line in parsed:
        direction, amount = line[0], int(line[1:])
        prev_dial = dial
        dial = dial - amount if direction == "L" else dial + amount
        clicks = abs(dial // 100)
        dial = dial % 100

        if direction == "L":
            if dial == 0:
                clicks += 1
            if prev_dial == 0:
                clicks -= 1

        count += clicks

    return count


if __name__ == "__main__":
    day = int(re.findall(r"\d+", __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ""
        content = read_input(day, in_file)
        parsed = content.splitlines()
        print(f"Part 1: {part1(parsed)}")
        print(f"Part 2: {part2(parsed)}")
