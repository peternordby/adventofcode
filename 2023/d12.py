import re
import sys
from functools import lru_cache

from utils import fetch_input, read_input


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

def part1(parsed):
    t = 0
    for _, line in enumerate(parsed):
        springs, nums = line.split()
        nums = [int(n) for n in nums.split(',')]
        nums = tuple(nums)
        combs = find_variations(springs, nums)
        t += combs
    return t

def part2(parsed):
    t = 0
    for _, line in enumerate(parsed):
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
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        parsed = content.splitlines()
        print(f'Part 1: {part1(parsed)}')
        print(f'Part 2: {part2(parsed)}')