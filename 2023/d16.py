import re
import sys

import numpy as np
from utils import fetch_input, read_input

directions = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0),
}

def step(pos, direction):
    return (pos[0] + directions[direction][0], pos[1] + directions[direction][1])

def beam(cave, start, direction):
    energized = set()
    loop_check = set()

    beams = [(start, direction)]
    
    while True:
        new_beams = []             

        if not beams: break

        for beam in beams:
            pos, direction = beam
            
            if pos[0] < 0 or pos[0] >= len(cave) or pos[1] < 0 or pos[1] >= len(cave[0]): continue

            # Add next position to energized
            energized.add(pos)

            # Check if we've been here before
            if (pos, direction) in loop_check:
                continue

            # Add to loop check so we don't go in circles
            loop_check.add((pos, direction))

            # Get next tile
            tile = cave[pos[0]][pos[1]]

            # Check if we need to change direction or split beam
            match tile:
                case '.':
                    # Continue beam
                    new_beams.append((step(pos, direction), direction))
                case '|':
                    # Split beam if we're going left or right, else continue beam
                    if direction in 'LR':
                        # Split beam
                        new_beams.append((step(pos, 'U'), 'U'))
                        new_beams.append((step(pos, 'D'), 'D'))
                    else:
                        # Continue beam
                        new_beams.append((step(pos, direction), direction))
                
                case '-':
                    # Split beam if we're going up or down, else continue beam
                    if direction in 'UD':  
                        # Split beam
                        new_beams.append((step(pos, 'L'), 'L'))
                        new_beams.append((step(pos, 'R'), 'R'))
                    else:
                        # Continue beam
                        new_beams.append((step(pos, direction), direction))
                    
                case '/':
                    # Change direction
                    match direction:
                        case 'R':
                            new_beams.append((step(pos, 'U'), 'U'))
                        case 'L':
                            new_beams.append((step(pos, 'D'), 'D'))
                        case 'U':
                            new_beams.append((step(pos, 'R'), 'R'))
                        case 'D':
                            new_beams.append((step(pos, 'L'), 'L'))

                case '\\':
                    # Change direction
                    match direction:
                        case 'R':
                            new_beams.append((step(pos, 'D'), 'D'))
                        case 'L':
                            new_beams.append((step(pos, 'U'), 'U'))
                        case 'U':
                            new_beams.append((step(pos, 'L'), 'L'))
                        case 'D':
                            new_beams.append((step(pos, 'R'), 'R'))
                           
        beams = new_beams
    return len(energized)

def part1(parsed):
    # Start beam at (0, 0) going right
    return beam(parsed, (0, 0), 'R')

def part2(parsed):
    all_energized = []

    # All left and right edges
    for r, row in enumerate(parsed):
        all_energized.append(beam(parsed, (r, 0), 'R'))
        all_energized.append(beam(parsed, (r, len(row) - 1), 'L'))

    # All top and bottom edges
    for c, col in enumerate(parsed[0]):
        all_energized.append(beam(parsed, (0, c), 'D'))
        all_energized.append(beam(parsed, (len(parsed) - 1, c), 'U'))

    return max(all_energized)
    

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        parsed = content.splitlines()
        print(f'Part 1: {part1(parsed)}')
        print(f'Part 2: {part2(parsed)}')