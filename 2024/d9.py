import re
import sys
from copy import deepcopy

from utils import fetch_input, read_input


def part1(content):
    disk = []

    for i, n in enumerate(content):
        # even = file_length
        if i%2 == 0:
            [disk.append(i//2) for _ in range(n)]
        # odd = free_space
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
        # even = file_length
        if i%2 == 0:
            [disk.append(i//2) for _ in range(n)]
        # odd = free_space
        else:
            [disk.append('.') for _ in range(n)]

    disk_i = len(disk) - 1
    fl_i = len(content) - 1


    # Find free space from left to right
    while 0 <= fl_i:
        print(disk)
        a = 0
        file_id = disk[disk_i]

        for i, n in enumerate(content):
            if i > fl_i:
                break

            # even = file_length
            if i%2 == 0:
                a += n
                continue
                
            # odd = free_space
            # if free space is big enough, replace free space with file indec
            elif n >= file_len:
                for j in range(file_len):
                    disk[a+j] = file_id
                    disk[disk_i-j] = "."
                a += n
                break

            a += n
            
        disk_i -= file_len
        disk_i -= content[fl_i-1]
        fl_i -= 2

    print(disk)


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