import re
import sys
from collections import deque
from math import lcm

import numpy as np
from utils import fetch_input, read_input

# % - Flip-Flop Module
# Initially off
# Flips state every time it receives a low signal
# Ignores high signals

# & - Conjunction Module
# Remember the type of signal received from EACH of its inputs
# Outputs a low signal if it receives high signals from ALL of its inputs
# Outputs a high signal otherwise

# Broadcast Module
# Outputs whatever signal it receives

# Button Module
# Outputs a low signal to broadcaster if pressed

class Module:
    def __init__(self, name, type, receivers):
        self.name = name
        self.type = type
        self.receivers = receivers

        if self.type == '%':
            self.memory = False
        elif self.type == '&':
            self.memory = {}
    
    def __repr__(self):
        return self.name + "{type=" + self.type + ",receivers=" + ",".join(self.receivers) + ",memory=" + str(self.memory) + "}"
    
def generate_modules(parsed):
    modules = {}
    broadcast_trgts = []

    for line in parsed:
        module, receivers = line.split(' -> ')
        receivers = receivers.split(', ')

        if module == 'broadcaster':
            broadcast_trgts = receivers
            continue

        name, type = module[1:], module[0]
        modules[name] = Module(name, type, receivers)

    for name, module in modules.items():
        for receiver in module.receivers:
            if receiver in modules and modules[receiver].type == '&':
                modules[receiver].memory[name] = False

    return modules, broadcast_trgts

def part1(parsed):
    
    modules, broadcast_trgts = generate_modules(parsed)
    
    low = 0
    high = 0

    for _ in range(1000):
        low += 1

        q = deque([('broadcaster', x, False) for x in broadcast_trgts])

        while q:
            origin, target, signal = q.popleft()

            low += 1 if not signal else 0
            high += 1 if signal else 0

            if target not in modules:
                continue

            module = modules[target]

            if module.type == '%':
                if not signal:
                    module.memory = not module.memory
                    for receiver in module.receivers:
                        q.append((target, receiver, module.memory))

            elif module.type == '&':
                module.memory[origin] = signal
                signal = not all(module.memory.values())
                for receiver in module.receivers:
                    q.append((target, receiver, signal))
    
    return low * high

def part2(parsed):

    modules, broadcast_trgts = generate_modules(parsed)

    (rx_in,) = [name for name, module in modules.items() if 'rx' in module.receivers]

    cycle_lengths = {}

    conjunction_ins = {name: 0 for name, module in modules.items() if rx_in in module.receivers}

    presses = 0

    while True:
        presses += 1

        q = deque([('broadcaster', x, False) for x in broadcast_trgts])

        while q:
            origin, target, signal = q.popleft()

            if target not in modules:
                continue

            module = modules[target]

            if module.name == rx_in and signal:
                conjunction_ins[origin] += 1

                if origin not in cycle_lengths:
                    cycle_lengths[origin] = presses

                if all(conjunction_ins.values()):
                    return lcm(*cycle_lengths.values())

            if module.type == '%':
                if not signal:
                    module.memory = not module.memory
                    for receiver in module.receivers:
                        q.append((target, receiver, module.memory))

            elif module.type == '&':
                module.memory[origin] = signal
                signal = not all(module.memory.values())
                for receiver in module.receivers:
                    q.append((target, receiver, signal))

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        parsed = content.splitlines()
        print(f'Part 1: {part1(parsed)}')
        print(f'Part 2: {part2(parsed)}')