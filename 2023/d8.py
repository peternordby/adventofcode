import re
import time

from utils import fetch_input


def read_input(TEST=0):
    filename = f"{__file__.split('.')[0]}{['', 'x1', 'x2'][TEST]}.txt"
    with open(filename) as f:
        puzzle = f.readlines()
    return puzzle

def part1(puzzle):
    dirs = puzzle[0].strip()

    mapping = {}

    for line in puzzle[2:]:
        line = line.strip()
        pos, nexts = line.split('=')
        pos = pos.strip()
        l, r = nexts.split(',')
        l = l.strip().replace('(', '')
        r = r.strip().replace(')', '')
        mapping[pos] = (l, r)

    pos = 'AAA'
    steps = 0
    start = time.time()
    interval = start
    while True:
        d = dirs[steps % len(dirs)]
        if d == 'R':
            pos = mapping[pos][1]
        elif d == 'L':
            pos = mapping[pos][0]
        steps += 1
        if steps % 1 == 10000:
            interval = time.time() - interval
            readable = round(interval, 3)
            total_so_far = round(time.time() - start, 3)
            print(f'{steps}: {pos} in {readable}s ({total_so_far}s total)')
            interval = time.time()
        if pos == 'ZZZ':
            return steps

def combine_phased_rotations(a_period, a_phase, b_period, b_phase):
    """Combine two phased rotations into a single phased rotation

    Returns: combined_period, combined_phase

    The combined rotation is at its reference point if and only if both a and b
    are at their reference points.
    """
    gcd, s, t = extended_gcd(a_period, b_period)
    phase_difference = a_phase - b_phase
    pd_mult, pd_remainder = divmod(phase_difference, gcd)
    if pd_remainder:
        raise ValueError("Rotation reference points never synchronize.")

    combined_period = a_period // gcd * b_period
    combined_phase = (a_phase - s * pd_mult * a_period) % combined_period
    return combined_period, combined_phase


def arrow_alignment(red_len, green_len, advantage):
    """Where the arrows first align, where green starts shifted by advantage"""
    period, phase = combine_phased_rotations(
        red_len, 0, green_len, -advantage % green_len
    )
    return -phase % period


def extended_gcd(a, b):
    """Extended Greatest Common Divisor Algorithm

    Returns:
        gcd: The greatest common divisor of a and b.
        s, t: Coefficients such that s*a + t*b = gcd

    Reference:
        https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
    """
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient, remainder = divmod(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t

def part2(puzzle):
    dirs = puzzle[0].strip()

    mapping = {}

    for line in puzzle[2:]:
        line = line.strip()
        pos, nexts = line.split('=')
        pos = pos.strip()
        l, r = nexts.split(',')
        l = l.strip().replace('(', '')
        r = r.strip().replace(')', '')
        mapping[pos] = (l, r)

    ends_with_A = [k for k in mapping.keys() if k[2] == 'A']
    ends_with_Z = [k for k in mapping.keys() if k[2] == 'Z']

    steps = 0
    all_steps = []
    pos = ends_with_A
    curr_steps = []

    for p in pos:
        while True:
            d = dirs[steps % len(dirs)]
            if d == 'R':
                p = mapping[p][1]
            elif d == 'L':
                p = mapping[p][0]
            steps += 1
            if p in ends_with_Z:
                curr_steps.append(steps)
                if len(curr_steps) == 2:
                    # print differences between steps
                    all_steps.append(curr_steps)
                    curr_steps = []
                    break

    from math import lcm
    return lcm(*[step[1]-step[0] for step in all_steps])
    

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        TEST = 0
        puzzle = read_input(TEST)
        print(f'Part 1: {part1(puzzle)}')
        print(f'Part 2: {part2(puzzle)}')