import copy
import os
import time

with open(__file__.replace('py', 'txt')) as f:
    puzzle = f.read().strip().splitlines()

example = '''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20'''.strip().splitlines()

example2 = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''.strip().splitlines()

def print_snake(next_rope: list, ind):
    for y in range(20, -20, -1):
        for x in range(-25, 25):
            if (x, y) in next_rope:
                i = next_rope.index((x,y))
                print(' ' + str(i) + ' ', end='')
            else:
                print('   ', end='')
        print('\n')
    print('\n')
    time.sleep(0.05)
    os.system('cls')

#puzzle = example

x, y = 0, 0
rope = [(0,0) for _ in range(10)]
next_rope = [(0,0) for _ in range(10)]
visited = set()
visited.add(rope[-1])

neighbours = [(1,-1), (1,0), (1,1), (0,-1), (0,0), (0,1), (-1, -1), (-1,0), (-1,1)]

for ind, line in enumerate(puzzle):
    cmd, num = line.split()
    num = int(num)
    
    if cmd == 'L':
        for _ in range(num):
            for i in range(len(rope)-1):
                if i == 0:
                    next_rope[i] = (rope[i][0]-1, rope[i][1])
                
                old_i = rope[i]
                new_i = next_rope[i]
                next_i = rope[i+1]

                diff = ((new_i[0]-next_i[0]), (new_i[1]-next_i[1]))
                if diff not in neighbours:
                    if i == 0:
                        next_rope[i+1] = old_i
                    else:
                        if diff in [(-1,2), (0,2), (1,2)]:
                            next_rope[i+1] = (new_i[0], new_i[1]-1)
                        
                        elif diff in [(-2,1), (-2,0), (-2,-1)]:
                            next_rope[i+1] = (new_i[0]+1, new_i[1])

                        elif diff in [(2,1), (2,0), (2,-1)]:
                            next_rope[i+1] = (new_i[0]-1, new_i[1])
                        
                        elif diff in [(-1,-2), (0,-2), (1,-2)]:
                            next_rope[i+1] = (new_i[0], new_i[1]+1)

                        elif diff == (-2,2):
                            next_rope[i+1] = (new_i[0]+1, new_i[1]-1)

                        elif diff == (2,2):
                            next_rope[i+1] = (new_i[0]-1, new_i[1]-1)

                        elif diff == (-2,-2):
                            next_rope[i+1] = (new_i[0]+1, new_i[1]+1)

                        elif diff == (2,-2):
                            next_rope[i+1] = (new_i[0]-1, new_i[1]+1)

                    if i+1 == 9:
                        visited.add(next_rope[i+1])
            rope = copy.deepcopy(next_rope)
            print_snake(next_rope, ind)

    if cmd == 'R':
        for _ in range(num):
            for i in range(len(rope)-1):
                if i == 0:
                    next_rope[i] = (rope[i][0]+1, rope[i][1])
                
                old_i = rope[i]
                new_i = next_rope[i]
                next_i = rope[i+1]

                diff = ((new_i[0]-next_i[0]), (new_i[1]-next_i[1]))
                if diff not in neighbours:
                    if i == 0:
                        next_rope[i+1] = old_i
                    else:
                        if diff in [(-1,2), (0,2), (1,2)]:
                            next_rope[i+1] = (new_i[0], new_i[1]-1)
                        
                        elif diff in [(-2,1), (-2,0), (-2,-1)]:
                            next_rope[i+1] = (new_i[0]+1, new_i[1])

                        elif diff in [(2,1), (2,0), (2,-1)]:
                            next_rope[i+1] = (new_i[0]-1, new_i[1])
                        
                        elif diff in [(-1,-2), (0,-2), (1,-2)]:
                            next_rope[i+1] = (new_i[0], new_i[1]+1)

                        elif diff == (-2,2):
                            next_rope[i+1] = (new_i[0]+1, new_i[1]-1)

                        elif diff == (2,2):
                            next_rope[i+1] = (new_i[0]-1, new_i[1]-1)

                        elif diff == (-2,-2):
                            next_rope[i+1] = (new_i[0]+1, new_i[1]+1)

                        elif diff == (2,-2):
                            next_rope[i+1] = (new_i[0]-1, new_i[1]+1)

                    if i+1 == 9:
                        visited.add(next_rope[i+1])
            rope = copy.deepcopy(next_rope)
            print_snake(next_rope, ind)
    
    if cmd == 'U':
        for _ in range(num):
            for i in range(len(rope)-1):
                if i == 0:
                    next_rope[i] = (rope[i][0], rope[i][1]+1)
                
                old_i = rope[i]
                new_i = next_rope[i]
                next_i = rope[i+1]

                diff = ((new_i[0]-next_i[0]), (new_i[1]-next_i[1]))
                if diff not in neighbours:
                    if i == 0:
                        next_rope[i+1] = old_i
                    else:
                        if diff in [(-1,2), (0,2), (1,2)]:
                            next_rope[i+1] = (new_i[0], new_i[1]-1)
                        
                        elif diff in [(-2,1), (-2,0), (-2,-1)]:
                            next_rope[i+1] = (new_i[0]+1, new_i[1])

                        elif diff in [(2,1), (2,0), (2,-1)]:
                            next_rope[i+1] = (new_i[0]-1, new_i[1])
                        
                        elif diff in [(-1,-2), (0,-2), (1,-2)]:
                            next_rope[i+1] = (new_i[0], new_i[1]+1)

                        elif diff == (-2,2):
                            next_rope[i+1] = (new_i[0]+1, new_i[1]-1)

                        elif diff == (2,2):
                            next_rope[i+1] = (new_i[0]-1, new_i[1]-1)

                        elif diff == (-2,-2):
                            next_rope[i+1] = (new_i[0]+1, new_i[1]+1)

                        elif diff == (2,-2):
                            next_rope[i+1] = (new_i[0]-1, new_i[1]+1)

                    if i+1 == 9:
                        visited.add(next_rope[i+1])
            rope = copy.deepcopy(next_rope)
            print_snake(next_rope, ind)
    
    if cmd == 'D':
        for _ in range(num):
            for i in range(len(rope)-1):
                if i == 0:
                    next_rope[i] = (rope[i][0], rope[i][1]-1)
                
                old_i = rope[i]
                new_i = next_rope[i]
                next_i = rope[i+1]

                diff = ((new_i[0]-next_i[0]), (new_i[1]-next_i[1]))
                if diff not in neighbours:
                    if i == 0:
                        next_rope[i+1] = old_i
                    else:
                        if diff in [(-1,2), (0,2), (1,2)]:
                            next_rope[i+1] = (new_i[0], new_i[1]-1)
                        
                        elif diff in [(-2,1), (-2,0), (-2,-1)]:
                            next_rope[i+1] = (new_i[0]+1, new_i[1])

                        elif diff in [(2,1), (2,0), (2,-1)]:
                            next_rope[i+1] = (new_i[0]-1, new_i[1])
                        
                        elif diff in [(-1,-2), (0,-2), (1,-2)]:
                            next_rope[i+1] = (new_i[0], new_i[1]+1)

                        elif diff == (-2,2):
                            next_rope[i+1] = (new_i[0]+1, new_i[1]-1)

                        elif diff == (2,2):
                            next_rope[i+1] = (new_i[0]-1, new_i[1]-1)

                        elif diff == (-2,-2):
                            next_rope[i+1] = (new_i[0]+1, new_i[1]+1)

                        elif diff == (2,-2):
                            next_rope[i+1] = (new_i[0]-1, new_i[1]+1)

                    if i+1 == 9:
                        visited.add(next_rope[i+1])
            rope = copy.deepcopy(next_rope)
            print_snake(next_rope, ind)


print(len(visited))

