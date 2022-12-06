input = '''1254117228
4416873224
8354381553
1372637614
5586538553
7213333427
3571362825
1681126243
8718312138
5254266347'''

test = '''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526'''

test2 = '''11111
19991
19191
19991
11111'''

flashed = []
octos = []
for row in input.split('\n'):
    octorow = []
    flashrow = []
    for octo in row:
        octorow.append(int(octo))
        flashrow.append(0)
    octos.append(octorow)
    flashed.append(flashrow)

# Ned, opp, venstre, høyre, ned venstre, opp venstre, ned høyre, opp høyre
nb_pos = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, 1), (-1, -1), (1, 1), (1, -1)]


def reset_and_count():
    flashes = 0
    for y in range(len(flashed)):
        for x in range(len(flashed[0])):
            if flashed[y][x] != 0:
                flashed[y][x] = 0
                flashes += 1
    return flashes


def flash(x, y):
    flashed[y][x] = 1
    for pos in nb_pos:
        try:
            if y+pos[1] >= 0 and x+pos[0] >= 0 and flashed[y+pos[1]][x+pos[0]] == 0:
                octos[y+pos[1]][x+pos[0]] += 1
                if octos[y+pos[1]][x+pos[0]] >= 10:
                    flash(x+pos[0], y+pos[1])
        except:
            continue


steps = 100
total = 0
step = 0
all_flashed = False
while not all_flashed:
    step += 1
    flashes = 0
    # First, the energy level of each octopus increases by 1
    for y in range(len(octos)):
        for x in range(len(octos[0])):
            octos[y][x] += 1
    # Then, any octopus with an energy level greater than 9 flashes.
    # This increases the energy level of all adjacent octopuses by 1, including octopuses that are diagonally adjacent.
    # If this causes an octopus to have an energy level greater than 9, it also flashes.
    # This process continues as long as new octopuses keep having their energy level increased beyond 9.
    # (An octopus can only flash at most once per step.)
    for y in range(len(octos)):
        for x in range(len(octos[0])):
            if octos[y][x] >= 10 and flashed[y][x] == 0:
                flash(x, y)
    for y in range(len(octos)):
        for x in range(len(octos[0])):
            if octos[y][x] >= 10:
                octos[y][x] = 0
    flashes = reset_and_count()
    total += flashes
    print(f'\n{flashes} flashes on step {step}')
    """ for row in octos:
        print("".join([str(i) for i in row])) """

    if flashes == len(octos) * len(octos[0]):
        all_flashed = True

print(total)

# 90 min ca del 1
# 2 min del 2
