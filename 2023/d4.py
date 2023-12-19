import re
import sys

from utils import fetch_input, read_input


def part1(parsed):
    total = 0
    for line in parsed:
        nums = line.split(':')[1]
        wins, mine = nums.split('|')
        wins = set([int(x.strip()) for x in wins.split(' ') if x != ''])
        mine = set([int(x.strip()) for x in mine.split(' ') if x != ''])
        same = wins.intersection(mine)
        if len(same) > 0:
            total += 2**(len(same)-1)
        

    return total


def part2(parsed):
    card = {}
    total = 0
    for i, line in enumerate(parsed):
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
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        parsed = content.splitlines()
        print(f'Part 1: {part1(parsed)}')
        print(f'Part 2: {part2(parsed)}')