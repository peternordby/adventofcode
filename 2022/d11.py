import math

import numpy as np

with open(__file__.replace('.py', '.txt')) as f:
    puzzle = f.read().strip().split('\n\n')

monkeys = {}
supermod = 1

for part in puzzle:
    lines = part.splitlines()
    monkey = int(lines[0].split()[1].strip(':'))
    starting = [int(x) for x in lines[1].split(':')[1].split(',')]
    operation = lines[2].split(':')[1].split()
    test = int(lines[3].split(':')[1].split()[2])
    if_true = int(lines[4].split(':')[1].split()[3])
    if_false = int(lines[5].split(':')[1].split()[3])

    monkeys[monkey] = {
        'starting': starting,
        'operation': operation,
        'test': test,
        'if_true': if_true,
        'if_false': if_false,
        'inspected': 0
        }

    supermod *= test


for round in range(10_000):
    print('Round', round)
    for monkey in range(len(puzzle)):
        # Adjust worry level
        for i, item in enumerate(monkeys[monkey]['starting']):
            # Add to inspected
            monkeys[monkey]['inspected'] += 1

            if monkeys[monkey]['operation'][3] == '*':
                if monkeys[monkey]['operation'][4] == 'old':
                    monkeys[monkey]['starting'][i] = item * item
                else:
                    monkeys[monkey]['starting'][i] = (item * int(monkeys[monkey]['operation'][4]))

            elif monkeys[monkey]['operation'][3] == '+':
                monkeys[monkey]['starting'][i] = (item + int(monkeys[monkey]['operation'][4]))

            # Mod by the product of all test integers
            monkeys[monkey]['starting'][i] = monkeys[monkey]['starting'][i] % supermod


        # Test worry level
        for i, item in enumerate(monkeys[monkey]['starting']):
            #if item % monkeys[monkey]['test'] == 0:
            if divmod(item, monkeys[monkey]['test'])[1] == 0:
                next_monkey = monkeys[monkey]['if_true']
            else:
                next_monkey = monkeys[monkey]['if_false']

            # Throw item
            monkeys[next_monkey]['starting'].append(item)

        # Delete items after throwing
        monkeys[monkey]['starting'] = []


totals = [monkeys[monkey]['inspected'] for monkey in monkeys]

print(totals)

max1 = max(totals)
totals.remove(max1)
max2 = max(totals)

print(max1*max2)