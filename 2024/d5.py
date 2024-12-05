import re
import sys

import numpy as np
from utils import fetch_input, read_input


def part1(rules, updates):
    ans = 0
    for update in updates:
        valid = True
        visited = set()
        order = [int(x) for x in update.split(",")]

        for number in order:
            if number in rules:
                if visited.intersection(rules[number]):
                    valid = False
                    break
            visited.add(number)

        if valid:
            ans += order[len(order)//2]

    return ans

def part2(rules, updates):
    ans = 0
    for update in updates:
        valid = True
        visited = set()
        order = [int(x) for x in update.split(",")]

        for number in order:
            if number in rules:
                if visited.intersection(rules[number]):
                    valid = False
                    break
            visited.add(number)

        if not valid:
            for x in order:
                print(x, len(rules[x].intersection(set(order))))
            order_copy = order.copy()
            order_copy.sort(key=lambda x: len(rules[x].intersection(set(order))), reverse=True)
            ans += order_copy[len(order_copy)//2]

    return ans

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        rules, updates = [x.splitlines() for x in content.split('\n\n')]
        rules_dict = {}
        for rule in rules:
            a, b = rule.split("|")
            a, b = int(a), int(b)
            if a in rules_dict:
                rules_dict[a].add(b)
            else:
                rules_dict[a] = set([b])
        rules = rules_dict
        print(f'Part 1: {part1(rules, updates)}')
        print(f'Part 2: {part2(rules, updates)}')