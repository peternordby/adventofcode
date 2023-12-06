import re

from utils import fetch_input


def read_input(TEST=0):
    filename = f"{__file__.split('.')[0]}{['', 'x1', 'x2'][TEST]}.txt"
    with open(filename) as f:
        puzzle = f.read()
    return puzzle

def part1(puzzle):
    maps = puzzle.split('\n\n')
    
    positions = [int(x) for x in maps[0].split(':')[1].strip().split(' ')]
    
    for i in range(1, len(maps)):
        lines = maps[i].split('\n')
        dsts, srcs, lengths = [], [], []
        for j in range(1, len(lines)):
            dst, src, length = [int(x) for x in lines[j].strip().split(' ')]
            dsts.append(dst)
            srcs.append(src)
            lengths.append(length)

        new_positions = []
        for pos in positions:
            for dst, src, length in zip(dsts, srcs, lengths):
                if src <= pos <= (src + length):
                    pos = dst + (pos - src)
                    break
            new_positions.append(pos)
        positions = new_positions

    return min(positions)

def part2(puzzle):
    maps = puzzle.split('\n\n')
    
    positions = [int(x) for x in maps[0].split(':')[1].strip().split(' ')]
    starts = positions[::2]
    range_lengths = positions[1::2]
    ends = [start + length for start, length in zip(starts, range_lengths)]

    ranges = list(zip(starts, ends))

    locations = []
    for (start, end) in ranges:
        ranges = [(start, end)]
        for m in maps[1:]:
            m = m.split('\n')[1:]
            inters = []
            for dst, src, sz in [tuple(map(int, x.split())) for x in m]:
                src_end = src + sz
                new_ranges = []
                while ranges:
                    (start, end) = ranges.pop()
                    before = (start, min(end, src))
                    inter = (max(start, src), min(src_end, end))
                    after = (max(src_end, start), end)
                    if before[1] > before[0]:
                        new_ranges.append(before)
                    if inter[1] > inter[0]:
                        inters.append((inter[0] - src + dst, inter[1] - src + dst))
                    if after[1] > after[0]:
                        new_ranges.append(after)
                ranges = new_ranges
            ranges = inters + ranges
        locations.append(min(ranges)[0])
    return min(locations)
    

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        TEST = 0
        puzzle = read_input(TEST)
        print(f'Part 1: {part1(puzzle)}')
        print(f'Part 2: {part2(puzzle)}')