import re
import sys

from utils import fetch_input, read_input


def part1(parsed):
    invalid = []
    for seq in parsed:
        a, b = seq.split("-")
        a, b = int(a), int(b)
        for i in range(a, b + 1):
            string = str(i)
            first = string[: len(string) // 2]
            second = string[len(string) // 2 :]
            if first == second:
                invalid.append(i)
    return sum(invalid)


def part2(parsed):
    invalid = set()
    for seq in parsed:
        a, b = seq.split("-")
        a, b = int(a), int(b)
        for i in range(a, b + 1):
            string = str(i)
            for substring_length in range(1, len(string) // 2 + 1):
                if len(string) // substring_length != 0:
                    parts = [
                        string[i : i + substring_length]
                        for i in range(0, len(string), substring_length)
                    ]
                    if len(set(parts)) == 1:
                        invalid.add(i)

    return sum(invalid)


if __name__ == "__main__":
    day = int(re.findall(r"\d+", __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ""
        content = read_input(day, in_file)
        parsed = content.split(",")
        print(f"Part 1: {part1(parsed)}")
        print(f"Part 2: {part2(parsed)}")
