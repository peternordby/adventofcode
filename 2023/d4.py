import re

from utils import fetch_input


def read_input(TEST=0):
    filename = f"{__file__.split('.')[0]}{['', 'x1', 'x2'][TEST]}.txt"
    with open(filename) as f:
        puzzle = f.readlines()
    return puzzle

def part1(puzzle):
    total = 0
    for line in puzzle:
        nums = line.split(':')[1]
        wins, mine = nums.split('|')
        wins = set([int(x.strip()) for x in wins.split(' ') if x != ''])
        mine = set([int(x.strip()) for x in mine.split(' ') if x != ''])
        same = wins.intersection(mine)
        if len(same) > 0:
            total += 2**(len(same)-1)
        

    return total


def part2(puzzle):
    card = {}
    total = 0
    for i, line in enumerate(puzzle):
        try:
            card[i+1] += 1
        except:
            card[i+1] = 1

        nums = line.split(':')[1]
        wins, mine = nums.split('|')
        wins = set([int(x.strip()) for x in wins.split(' ') if x != ''])
        mine = set([int(x.strip()) for x in mine.split(' ') if x != ''])
        same = wins.intersection(mine)

        for j in range(len(same)):
            try:
                card[i+j+2] += card[i+1]
            except:
                card[i+j+2] = card[i+1]
        
    for k, v in card.items():
        total += v

    return total

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        TEST = 0
        puzzle = read_input(TEST)
        print(f'Part 1: {part1(puzzle)}')
        print(f'Part 2: {part2(puzzle)}')