import re
import time
from functools import lru_cache

from utils import fetch_input


def read_input(TEST=0):
    filename = f"{__file__.split('.')[0]}{['', 'x1', 'x2'][TEST]}.txt"
    with open(filename) as f:
        puzzle = f.readlines()
    return puzzle


@lru_cache
def find_variations(springs, nums):
    if springs == "":
        return 1 if nums == () else 0
    
    if nums == ():
        return 0 if '#' in springs else 1
    
    result = 0
    if springs[0] in '.?':
        result += find_variations(springs[1:], nums)

    if springs[0] in '#?':
        if nums[0] <= len(springs) and "." not in springs[:nums[0]] and (nums[0] == len(springs) or springs[nums[0]] != "#"):
            result += find_variations(springs[nums[0] + 1:], nums[1:])

    return result    

def part1(puzzle):
    t = 0
    for i, line in enumerate(puzzle):
        springs, nums = line.split()
        nums = [int(n) for n in nums.split(',')]
        nums = tuple(nums)
        combs = find_variations(springs, nums)
        t += combs
    return t

def part2(puzzle):
    t = 0
    for i, line in enumerate(puzzle):
        springs, nums = line.split()
        springs = '?'.join([springs]*5)
        nums = [int(n) for n in nums.split(',')]*5
        nums = tuple(nums)
        combs = find_variations(springs, nums)
        t += combs
    return t

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        TEST = 0
        puzzle = read_input(TEST)
        print(f'Part 1: {part1(puzzle)}')
        print(f'Part 2: {part2(puzzle)}')