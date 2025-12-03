import re
import sys

from utils import fetch_input, read_input


def find_largest(sublist: list[int], last_index: int):
    return max(sublist), sublist.index(max(sublist)) + last_index


def part1(parsed):
    ans = 0
    for pack in parsed:
        pack = [int(x) for x in pack]
        first, first_i = find_largest(pack[:-1], 0)
        second = max(pack[first_i + 1 :])

        ans += int("".join([str(x) for x in [first, second]]))

    return ans


def part2(parsed):
    ans = 0
    for pack in parsed:
        pack = [int(x) for x in pack]
        joltages = []
        ji = 0
        for i in range(11, -1, -1):
            if i == 0:
                j, ji = find_largest(pack[ji:], ji + 1)
            else:
                j, ji = find_largest(pack[ji:-i], ji + 1)
            joltages.append(j)

        ans += int("".join([str(x) for x in joltages]))
    return ans


if __name__ == "__main__":
    day = int(re.findall(r"\d+", __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ""
        content = read_input(day, in_file)
        parsed = content.splitlines()
        print(f"Part 1: {part1(parsed)}")
        print(f"Part 2: {part2(parsed)}")
