import re

from utils import fetch_input


def read_input(TEST=0):
    filename = f"{__file__.split('.')[0]}{['', 'x1', 'x2'][TEST]}.txt"
    with open(filename) as f:
        puzzle = f.readlines()
    return puzzle

def get_neighbors(puzzle, y, x):
    neighbors = []
    neighbors_pos = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            try:
                neighbors.append(puzzle[y+i][x+j])
                neighbors_pos.append((y+i, x+j))
            except:
                continue
    return neighbors, neighbors_pos

num_positions = []

def part1(puzzle):
    total = 0
    global num_positions
    
    for y, line in enumerate(puzzle):
        cur_xys = []
        cur = ''
        for x, char in enumerate(line):
            if char.isdigit():
                cur += char
                cur_xys.append((y, x))
            elif len(cur) > 0:
                num = int(cur)
                valid = False
                for pos in cur_xys:
                    if valid: break
                    neighbors = get_neighbors(puzzle, *pos)[0]
                    for neighbor in neighbors:
                        if not neighbor.isdigit() and neighbor != '.' and neighbor != '\n':
                            valid = True
                            total += num
                            break
                # print(f'{cur} is {valid} {total}')
                num_positions.append((cur_xys, num))
                cur_xys = []
                cur = ''

            
    return total

def part2(puzzle):
    total = 0

    for y, line in enumerate(puzzle):
        for x, char in enumerate(line):
            if char == '*':
                valid_neighbors = []
                for pos in num_positions:
                    neigh, neigh_pos = get_neighbors(puzzle, y, x)
                    for i, npos in enumerate(neigh_pos):
                        if not neigh[i].isdigit():
                            continue
                        if npos in pos[0]:
                            valid_neighbors.append(pos[1])
                            continue
                valid_neighbors = list(set(valid_neighbors))
                if len(valid_neighbors) == 2:
                    total += valid_neighbors[0] * valid_neighbors[1]

    return total

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        TEST = 0
        puzzle = read_input(TEST)
        print(f'Part 1: {part1(puzzle)}')
        print(f'Part 2: {part2(puzzle)}')