import re
import sys

from utils import fetch_input, read_input


def part1(parsed):
    total = 0
    for line in parsed:
        digits = []
        for char in line:
            if char.isdigit():
                digits.append(int(char))
        total += digits[0]*10+digits[-1]
    
    return total
    

def part2(parsed):
    spelling = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four' : 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine' : 9,
    }

    total = 0
    for line in parsed:
        digits = []
        i = 0
        while i < len(line):
            if line[i].isdigit():
                digits.append(int(line[i]))
                i += 1
            elif line[i:i+3] in spelling:
                digits.append(spelling[line[i:i+3]])
                i += 1
            elif line[i:i+4] in spelling:
                digits.append(spelling[line[i:i+4]])
                i += 1
            elif line[i:i+5] in spelling:
                digits.append(spelling[line[i:i+5]])
                i += 1
            else:
                i += 1
        total += digits[0]*10+digits[-1]

    return total

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        parsed = content.splitlines()
        print(f'Part 1: {part1(parsed)}')
        print(f'Part 2: {part2(parsed)}')