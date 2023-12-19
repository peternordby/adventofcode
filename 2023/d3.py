import re
import sys

from utils import fetch_input, read_input


def get_neighbors(grid, y, x):
    neighbors = []
    neighbors_pos = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            try:
                neighbors.append(grid[y+i][x+j])
                neighbors_pos.append((y+i, x+j))
            except:
                continue
    return neighbors, neighbors_pos

num_positions = []

def part1(parsed):
    total = 0
    global num_positions
    
    for y, line in enumerate(parsed):
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
                    neighbors = get_neighbors(parsed, *pos)[0]
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

def part2(parsed):
    total = 0

    for y, line in enumerate(parsed):
        for x, char in enumerate(line):
            if char == '*':
                valid_neighbors = []
                for pos in num_positions:
                    neigh, neigh_pos = get_neighbors(parsed, y, x)
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
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        parsed = content.splitlines()
        print(f'Part 1: {part1(parsed)}')
        print(f'Part 2: {part2(parsed)}')