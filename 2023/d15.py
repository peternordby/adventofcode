import re

from utils import fetch_input


def read_input(TEST=0):
    filename = f"{__file__.split('.')[0]}{['', 'x1', 'x2'][TEST]}.txt"
    with open(filename) as f:
        puzzle = f.read().split(',')
    return puzzle

def HASH(string):
    curr = 0
    for char in string:
        ascii_code = ord(char)
        curr += ascii_code
        curr *= 17
        curr = curr % 256
    return curr

def HASHMAP(string: str, boxes: dict):
    if '-' in string:
        label = string[:-1]
        box = HASH(label)
        if box not in boxes:
            return
        for idx, (l, _) in enumerate(boxes[box]):
            if l == label:
                del boxes[box][idx]
                break

    if '=' in string:
        label, focal = string.split('=')
        box = HASH(label)
        if box not in boxes:
            boxes[box] = []
        for idx, (l, _) in enumerate(boxes[box]):
            if l == label:
                boxes[box][idx] = (label, focal)
                break
        else:
            boxes[box].append((label, focal))

def part1(puzzle):
    return sum([HASH(string) for string in puzzle])

def part2(puzzle):
    boxes = {}
    [HASHMAP(string, boxes) for string in puzzle]

    focusing_power = 0

    order = sorted(boxes.keys())
    for box in order:
        for i, (_, focal) in enumerate(boxes[box]):
            focal = int(focal)
            focusing_power += (box + 1) * (i + 1) * focal

    return focusing_power

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        TEST = 0
        puzzle = read_input(TEST)
        print(f'Part 1: {part1(puzzle)}')
        print(f'Part 2: {part2(puzzle)}')