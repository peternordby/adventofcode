import re
import sys
from functools import cache

import numpy as np
from utils import fetch_input, read_input


def part1(parsed, blinks: int):
    stones = [int(x) for x in parsed]

    def blink(stones):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                new_stones.append(int(str(stone)[:len(str(stone))//2]))
                new_stones.append(int(str(stone)[len(str(stone))//2:]))
            else:
                new_stones.append(stone*2024)
        return new_stones
    
    for _ in range(blinks):
        stones = blink(stones)

    return len(stones)

def part2(parsed, blinks: int):
    stones = [int(x) for x in parsed]
    
    @cache
    def blink_stone(stone: int, depth = 0):
        if depth >= blinks:
            return 1
        count = 0
        if stone == 0:
            count += blink_stone(1, depth=depth+1)
        elif len(str(stone)) % 2 == 0:
            count += blink_stone(int(str(stone)[:len(str(stone))//2]), depth=depth+1)
            count += blink_stone(int(str(stone)[len(str(stone))//2:]), depth=depth+1)
        else:
            count += blink_stone(stone*2024, depth=depth+1)
        
        return count

    return sum([blink_stone(stone, depth=0) for stone in stones])

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        parsed = content.split()
        print(f'Part 1: {part1(parsed, 25)}')
        print(f'Part 2: {part2(parsed, 75)}')