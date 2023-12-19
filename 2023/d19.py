import re
import sys

import numpy as np
from utils import fetch_input, read_input


def eval_rule(part, rule):
    if ':' not in rule:
        return rule
    
    comparison, wf = rule.split(':')
    if '<' in comparison:
        attr, val = comparison.split('<')
        if part[attr] < int(val):
            return wf
        else:
            return None
    elif '>' in comparison:
        attr, val = comparison.split('>')
        if part[attr] > int(val):
            return wf
        else:
            return None
        
def split_range(xmas_range, rule):
    if ':' not in rule:
        new_range = xmas_range.copy()
        
        new_range['wf'] = rule
        new_range['rule_idx'] = 0

        return new_range
    
    comparison, new_wf = rule.split(':')
    if '<' in comparison:
        attr, val = comparison.split('<')

        left_range = xmas_range.copy()
        right_range = xmas_range.copy()

        # (a, b, 'wf', 'rule_idx') -> 
        # left_range -> (a, val, 'new_wf', 0)
        # right_range -> (val, b, 'wf', rule_idx+1)

        left_range[attr] = [left_range[attr][0], int(val)]
        left_range['wf'] = new_wf
        left_range['rule_idx'] = 0

        right_range[attr] = [int(val), right_range[attr][1]]
        right_range['rule_idx'] += 1

        return left_range, right_range
        
    elif '>' in comparison:
        attr, val = comparison.split('>')

        left_range = xmas_range.copy()
        right_range = xmas_range.copy()

        # (a, b, 'wf', 'rule_idx') -> 
        # left_range -> (val, b, 'new_wf', 0)
        # right_range -> (a, val, 'wf', rule_idx+1)

        left_range[attr] = [int(val)+1, left_range[attr][1]]
        left_range['wf'] = new_wf
        left_range['rule_idx'] = 0

        right_range[attr] = [right_range[attr][0], int(val)+1]
        right_range['rule_idx'] += 1

        return left_range, right_range
    

def part1(parsed):
    rules = parsed[0].splitlines()
    parts = parsed[1].splitlines()

    wfs = {}

    for rule in rules:
        wf, rs = rule.split('{')
        rs = rs[:-1].split(',')
        wfs[wf] = rs

    accepted = []

    for part in parts:
        part = part[1:-1].split(',')
        part = {p.split('=')[0]: int(p.split('=')[1]) for p in part}
        wf = 'in'
        finished = False
        while not finished:
            for rule in wfs[wf]:
                nwf = eval_rule(part, rule)
                if nwf == 'A':
                    accepted.append(part)
                    finished = True
                    break
                elif nwf == 'R':
                    finished = True
                    break
                elif not nwf:
                    continue
                else:
                    wf = nwf
                    break

    t = 0
    for part in accepted:
        for attr in part:
            t += part[attr]

    return t

def part2(parsed):
    rules = parsed[0].splitlines()

    wfs = {}

    for rule in rules:
        wf, rs = rule.split('{')
        rs = rs[:-1].split(',')
        wfs[wf] = rs

    ranges = [{
        'wf': 'in',
        'rule_idx': 0,
        'x': [1, 4001],
        'm': [1, 4001],
        'a': [1, 4001],
        's': [1, 4001],
    }]

    approved_ranges = []

    while ranges:
        new_ranges = []
        for xmas_range in ranges:
            wf = xmas_range['wf']
            rule_idx = xmas_range['rule_idx']
            rule = wfs[wf][rule_idx]
            split = split_range(xmas_range, rule)

            if isinstance(split, tuple):
                for new_range in split:
                    if new_range['wf'] == 'A':
                        approved_ranges.append(new_range)
                    elif new_range['wf'] == 'R':
                        continue
                    else:
                        new_ranges.append(new_range)

            elif isinstance(split, dict):
                if split['wf'] == 'A':
                    approved_ranges.append(split)
                elif split['wf'] == 'R':
                    continue
                else:
                    new_ranges.append(split)

        ranges = new_ranges

    t = 0
    for xmas_range in approved_ranges:
        prod = 1
        xmas_attrs = 'xmas'
        for attr in xmas_attrs:
            start, end = xmas_range[attr] 
            print(f'{attr}: {start}\t- {end}', end='\t')
            prod *= (end - start)
        print()
        t += prod

    return t

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        parsed = content.split('\n\n')
        print(f'Part 1: {part1(parsed)}')
        print(f'Part 2: {part2(parsed)}')