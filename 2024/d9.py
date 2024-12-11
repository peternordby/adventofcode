import re
import sys
from copy import deepcopy

from utils import fetch_input, read_input


def part1(content):
    disk = []

    for i, n in enumerate(content):
        if i%2 == 0:
            [disk.append(i//2) for _ in range(n)]
        else:
            [disk.append('.') for _ in range(n)]

    a = 0
    b = len(disk)-1
    new_disk = []

    while a <= b:
        if disk[a] != '.':
            new_disk.append(disk[a])
            a += 1
            continue
        
        while disk[b] == '.':
            b -= 1

        new_disk.append(disk[b])
        a += 1
        b -= 1

    ans = 0
    for i, n in enumerate(new_disk):
        ans += i*n

    return ans

def part2(content):
    disk = []

    for i, n in enumerate(content):
        if i%2 == 0:
            [disk.append(i//2) for _ in range(n)]
        else:
            [disk.append('.') for _ in range(n)]


    x = len(content) - 1
    end = len(disk)
    f_len = content[x]

    while end > 0:
        start = end - f_len

        i = 0
        while i < start:
            space = disk[i:i+f_len]
            if all([c == "." for c in space]):
                disk = disk[:i] + disk[start:end] + disk[i+f_len:start] + disk[i:i+f_len] + disk[end:]
                break
            i += 1

        x -= 1
        end -= f_len
        end -= content[x]
        x -= 1
        f_len = content[x]

    ans = 0
    for i, n in enumerate(disk):
        if n != ".":
            ans += i*n

    return ans

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        in_file = sys.argv[1] if len(sys.argv) > 1 else ''
        content = read_input(day, in_file)
        content = [int(x) for x in content]
        print(f'Part 1: {part1(content)}')
        print(f'Part 2: {part2(content)}')