import re

from utils import fetch_input


def read_input(TEST=0):
    filename = f"{__file__.split('.')[0]}{['', 'x1', 'x2'][TEST]}.txt"
    with open(filename) as f:
        puzzle = f.readlines()
    return puzzle

def part1(puzzle):
    total = 0
    reds = 12
    greens = 13
    blues = 14

    for i, game in enumerate(puzzle):
        colors = {
            'red': [],
            'green': [],
            'blue': []
        }
        game_id = i+1
        cubes = game.split(': ')[1]
        cubes = cubes.split(' ')
        i = 0
        while i < len(cubes):
            num = int(cubes[i])
            col = cubes[i+1].replace(',', '').replace(';', '').replace('\n', '')
            colors[col].append(num)
            i += 2

        if reds >= max(colors['red']) and greens >= max(colors['green']) and blues >= max(colors['blue']):
            total += game_id

    return total

def part2(puzzle):
    total = 0
    for i, game in enumerate(puzzle):
        colors = {
            'red': [],
            'green': [],
            'blue': []
        }
        game_id = i+1
        cubes = game.split(': ')[1]
        cubes = cubes.split(' ')
        i = 0
        while i < len(cubes):
            num = int(cubes[i])
            col = cubes[i+1].replace(',', '').replace(';', '').replace('\n', '')
            colors[col].append(num)
            i += 2

        r, g, b = max(colors['red']), max(colors['green']), max(colors['blue'])
        po = r*g*b
        total += po

    return total

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        TEST = 0
        puzzle = read_input(TEST)
        print(f'Part 1: {part1(puzzle)}')
        print(f'Part 2: {part2(puzzle)}')