import re
import sys

from utils import fetch_input, read_input


def start_value(op):
    match op:
        case "+":
            return 0
        case "*":
            return 1
        case _:
            raise TypeError


def part1(parsed):
    ops = parsed[-1].split()
    table = []
    for line in parsed[:-1]:
        table.append([int(x) for x in line.split()])

    ans = 0
    for i, op in enumerate(ops):
        res = start_value(op)
        if op == "+":
            for line in table:
                res += line[i]
        elif op == "*":
            for line in table:
                res *= line[i]
        ans += res

    return ans


def part2(parsed):
    ops = parsed[-1].split()
    table = parsed[:-1]

    ans = 0
    opi = len(ops) - 1
    op = ops[opi]
    res = start_value(op)
    for i in range(len(table[0]) - 1, -1, -1):
        num_string = ""
        for line in table:
            if line[i] == " ":
                continue
            else:
                num_string += line[i]
        if num_string == "":
            opi -= 1
            if opi < 0:
                break
            op = ops[opi]
            ans += res
            res = start_value(op)
        else:
            if op == "+":
                res += int(num_string)
            elif op == "*":
                res *= int(num_string)
    ans += res

    return ans


if __name__ == "__main__":
    day = int(re.findall(r"\d+", __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ""
        content = read_input(day, in_file)
        parsed = content.splitlines()
        print(f"Part 1: {part1(parsed)}")
        print(f"Part 2: {part2(parsed)}")
