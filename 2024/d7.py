import re
import sys
from itertools import combinations, product

import numpy as np
from utils import fetch_input, read_input


def calculate(comb, bit_comb, target):
        res = comb[0]
        for num, bit in zip(comb[1:], bit_comb):
            match bit:
                case 0:
                    res += num
                case 1:
                    res *= num
                case 2:
                    res = int(str(res)+str(num))
            if res > target:
                break
        return res

def part1(parsed):
    ans = 0

    for line in parsed:
        target, nums = line.split(":")
        target = int(target)
        nums = [int(num) for num in nums.split()]

        combs = [x for x in combinations(nums, len(nums))]

        found = False
        for comb in combs:
            if found:
                break
            bit_combs = list(product([0, 1], repeat=len(comb)-1))
            for bit_comb in bit_combs:
                res = calculate(comb, bit_comb, target)
                if res == target:
                    ans += target
                    found = True
                    break

    return ans

def part2(parsed):
    ans = 0

    for line in parsed:
        target, nums = line.split(":")
        target = int(target)
        nums = [int(num) for num in nums.split()]

        combs = [x for x in combinations(nums, len(nums))]

        found = False
        for comb in combs:
            if found:
                break
            bit_combs = list(product([0, 1, 2], repeat=len(comb)-1))
            for bit_comb in bit_combs:
                res = calculate(comb, bit_comb, target)
                if res == target:
                    ans += target
                    found = True
                    break

    return ans

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        parsed = content.splitlines()
        print(f'Part 1: {part1(parsed)}')
        print(f'Part 2: {part2(parsed)}')