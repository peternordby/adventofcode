with open(__file__.replace('py', 'txt')) as f:
    puzzle = f.read().strip().splitlines()

""" with open(__file__.replace('.py', 'ex.txt')) as f:
    puzzle = f.read().strip().splitlines() """

# Part 1
""" x = 1
cycle = 1
count = 0
singal_strengths = []
for line in puzzle:
    splitted = line.split()
    if splitted[0] == 'noop':
        cycle += 1
        count += 1
        if count == 40 or cycle == 20:
            singal_strengths.append(cycle*x)
            count = 0
    
    elif splitted[0] == 'addx':
        cycle += 1
        count += 1
        if count == 40 or cycle == 20:
            singal_strengths.append(cycle*x)
            count = 0

        x += int(splitted[1])

        cycle += 1
        count += 1
        if count == 40 or cycle == 20:
            singal_strengths.append(cycle*x)
            count = 0

print(singal_strengths)
print(sum(singal_strengths)) """

def draw_crt(sprite, crt, cycle):
    if cycle in sprite:
        crt.append('#')
    else:
        crt.append('.')

x = 1
cycle = 0
sprite = [0, 1, 2]
crts = []
crt = []
for line in puzzle:
    splitted = line.split()
    if splitted[0] == 'noop':
        #Cycle
        draw_crt(sprite, crt, cycle)
        cycle += 1
        if cycle == 40:
            cycle = 0
            crts.append(crt)
            crt = []
    
    elif splitted[0] == 'addx':
        #Cycled
        draw_crt(sprite, crt, cycle)
        cycle += 1
        if cycle == 40:
            cycle = 0
            crts.append(crt)
            crt = []

        #Cycle
        draw_crt(sprite, crt, cycle)
        cycle += 1
        if cycle == 40:
            cycle = 0
            crts.append(crt)
            crt = []
        
        arg = int(splitted[1])
        sprite = [sprite[0]+arg, sprite[1]+arg, sprite[2]+arg]
   

i = 0
for crt in crts:
    for char in crt:
        print(char, end='')
    print()