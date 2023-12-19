import re
import sys

from utils import fetch_input, read_input


def find_diffs(seq: list):
    diffs = []
    for i in range(len(seq)-1):
        diffs.append(seq[i+1] - seq[i])
    return diffs

def part1(parsed):
    preds = []
    for l in parsed:
        lasts = []
        seq = l.split()
        seq = [int(x) for x in seq]
        orig = seq.copy()
        seq = find_diffs(seq)
        lasts.append(seq[-1])
        while not all([x == 0 for x in seq]):
            seq = find_diffs(seq)
            lasts.append(seq[-1])
        pred = 0
        while lasts:
            last = lasts.pop()
            pred += last
        preds.append(pred + orig[-1])
    return sum(preds)

def part2(parsed):
    preds = []
    for l in parsed:
        firsts = []
        seq = l.split()
        seq = [int(x) for x in seq]
        orig = seq.copy()
        seq = find_diffs(seq)
        firsts.append(seq[0])
        while not all([x == 0 for x in seq]):
            seq = find_diffs(seq)
            firsts.append(seq[0])
        pred = 0
        while firsts:
            last = firsts.pop()
            pred = last - pred
        preds.append(orig[0] - pred)
    return sum(preds)

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        parsed = content.splitlines()
        print(f'Part 1: {part1(parsed)}')
        print(f'Part 2: {part2(parsed)}')