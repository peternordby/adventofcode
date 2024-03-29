import copy

input = '''########.###.##.##..##..#...##..##..####.##...##..#.#.#####....#....##..##.##.##..#.##...##..#...##...#.#.####...#.###..#..#.#....####.........#.....#.....#..#.#..#..##..######..#.#.###..#...#.##....#.##.##..###.##.#..#..#####..##..##.....#.##.######..#.#...#..#.....#..#..##...##.#.###....#.#.#.#.####.##.####.##.#.#.....##..##.#...####....#..#..##.#...#..#.##.....#.#.##.###..#.#........#.#######..#..#..##.########........###.############...#...##.#######.##.########..#...#..#........#...###.#.##.#..#.####..

...#....##.###...##.#..#....#.###.##.....#..#...###....#.###..###.##.#.#.#.....#....#...##...#..#..#
.#...#.#.#.####..#...#..#.#..###.##..#.####...#....###..###...#.##.#...#....#.#..##.#....#...####.#.
#####.#.#..##..##..#.#.###.#..##.##.##.##.....#..#....#.#.##.#.##.#..#.####...#.#.##..##.####..##..#
...##.#...######.#..##..###...##..#.##.##.#..#####.##.#..##..#.#####.##...#.#.#..##.#.#......#..##..
##.#...#..#.#.#....#..#.##.###..#...#.#.....###.#...###.#....#.##..###.#..#.##..#.##.#..#....##..###
..#...##.#####..#.#.###....##.#.#..#.###.##.#####.##.....##...#......#..#.###.#.....###...####...#..
.##.##.###.#.#...#..#####...#..##.#.#.##...#.##.#.#..###.#.####......#.#.##..#...#.##..#####...##..#
....#.#..#.......#.#.#..###.####.#.#.#.###...##..###..#.######...####..###....##.#...##.#..########.
...........#....###.#...##.#.##..##..##...#.#...###.#..###.#.......#........#.##..##.....#.##.#.###.
.##.##..##...#.#.#...#.#.##.###.##..#.##.##.....######.##.....#....##....#..##.#....#..#######......
#........####.#....#####.#..#..##...#.#.#####.#....##.#.##.##...#.#####.......#..###.#.###.####...##
..####..#.#....######..###.#......##...#####.####.#.#.#######..#.###...##..#..#..##.#...#.....##.###
####.#...####.##...#...#####...#######...#.#.##.#.##......##..###.#.#.##.#.###...#..#.###.##..##.#..
..#.#...#.#.....#.#.##.###..##..#.#.##..###.....#..##......###.......#.##.##...####.#...###.....#...
..##.######.#...#..##.###.#.#.....##......#..#......##.###.###.#.....#.#..##.###.#.#.#...#.#.###.#..
##.#.#.###.#.##.#..####..##..#...###.#####.###.####.#.##.#..#.##.######....#.#.#...#.#.#......##..#.
..###.#.##########.##...##..#.###.#...##...##..#...#..#.##.#....##.######...####....####.#...##.#..#
####...#.#...#.#..#.#.#.....#.#.#..##....#.....###..#....#..#.#.##.#...#..#.###.#..##.#..##.#....#..
##.####.#....#.##.#.#..#####.#.......#.####..#.#...###....###.#.###.#..#.###.#..####.#...#.#..#.#...
#.###..#...###.#.#.####..#.#.##.#..###.#####..#........#..#.....##.#.#...######.#..##....###.##.##.#
#..#.#..##.######.######.#.#.###...#....###.##..#.#.#.##.##..#.#...#..#..###....#......##...#######.
#.####..#..##.#.###.#..##...####..#.##.#####..##.#..####..#.#..#.##..###...#..#..#.###.######.####..
..##..#.##...#..##....#..##...##..##..#.###.#.###....##..###.........#..#.##.#..#......#.#####.##.##
#.##........####..#....#..#..####.######..#.######.......#.###.#.##...#.#..#.#.#.#####.#.##....#...#
#.#.#......#.##.#.#....#.#..#.#.##...#...###..###.#.#...##...#....#.#.#..###...#.#..##.#.##.#....###
.#....#####.#...##.#.########...###.#####.#.#....####..#.#...###.##...#..#.#....#.##..#.#.#####.#...
.#..##.#......##.####..##..#..##....##.##.###..#..##.#...####..##...##...#..#...####..####.#.#.##.##
.#...###..####..#.##....##.#..#...###...#.#..#.#..##.....##...#.##...#.#.######.#.##.....#.###......
...#.#....#..############.##...#.#...##..###..#..#.##.####.###.#.##..##.###..#..###.####..#....####.
....###..#.##.####..#...##.##.###...#..#.#.##.#..#.#.##..#..........#.##....#.###.#######..##.#.#.##
###.#.##.##.#####..#.###.#.#.#.#####.#.##...##...#.#.#############....####.###....#####.....#..##.##
#######.#.....####.#..#.###..##...##.#..##.....#.##.....########....#..##.####.###..#..##......#..##
...#.#.#...####.#.###.......#...##..###...##...####.#...###..##...#..###.##.#####.####.#...#...#####
##.##.#.#.#.#.....##.##.##.####.#.#...###..#..#....#...#..........##.###.#..#.###.######.##..#..#...
##...#..####..#.##.###...#.#.##..##.#.##..##...#.#..###...#....#....###.###.#.#.#####....#.###.#.###
.....##.#..#.######.#.#.##.###...#..#...#.....#.##.####..##..##.###.#########....#...#.#..##..###...
.#...#######.#..#.#..#.##########...##.#.##....########..#.####.#.###.##..#..#..#.#..#.#.#######.#.#
.#..#..#..#.##....#.....#.##.#.###.###..####..##..##..#.#.#.#.#.##..#.#..#.########.##.####...###...
##.#.#..#.#.#.#.#...#.###.#.####.####.#..##..#.#.#.####.#...#.###.#.######..#.#####.##..##..#..####.
##....#..#.####.#..#...#...########.#.#.#####.###.###..##..##.##.....#.....####.##...#.##.#....#..#.
.##.##...###...#.##.##...###.####.#..##.#.###.####.#.....####..#.##.##..###.##.#.#.#.##..#.....#...#
.##..####..#..###..#...##..#.........#...####.#.#######....##..#...#.....##..#.#.#..#.##.##.##..##..
##.###.###.##..####.#......#.#....#.####.#####....#.#.#....##.###...#.#...##.##...#####.#####..#.#..
####.##....##.###....#.#..##.#####.##.#.##..####...##...##.###.#..#.##...#.####.###...########......
###.####.##..#...###...######.###..##.#.#.#.#.#.#....#.####...#..#.....##...#.##...#.#..#.#......##.
...##..#....#.#...#..##....#.....##..#.#...#.###.#..#.#..#......##.##..#.##....####.#..#.###...##...
##..#.##...#..##....#.#.....#..#.###........###...#..######...#..###...##...####.#.#..##.###.......#
.###...#.###...#..####.#.##.##.##...#...#..##.#....##....###..#...##..###...#....##.#...###..#.#.###
...#..#..#.#...##.##.##...#####.#.######..#..#...##.#...#.#....###.#.#.####..#....#..#.#..####...#..
#...#..####.##.##....##.#.#.##.#.......###.#.##..##...#.#..##.#.####.#..##.##...#..#.###..##.......#
###..##.#..#.#...#.#......#.##.#.##..#..#...#....#.....#..##..#..#..###.#..#...#.#.....#.###......##
#..##.#####.#.##.####.......#.#..#.##...#.#.#....#.#.######...##...##...####.#..#..#.###.#.#...####.
....#.#.##.#.##.#.##.###.#.###..#####.#.###.##..#.#..##....###...##...#.#..#.##..####.###.######.#.#
..###.##.....#.#.####.##.#.#.##.#####...##.#.##.###.#..##.###.#.###.........##....##.#.##....#.##...
##...#.#..#.#.#.###.###.#...#.#..#..#...###.###..####....####.........#..#####.##..#..##...##.##...#
.#..#..#.##.###.#...#...#...#.##...#...##....###.......#.#####..#..###...######..##..##.##.#.#.###.#
..#...#.##.##.####....##.#..#.##.##.#.##.#.#...#.#.#####......###...#..#.#...#.#..###.####...##.#.#.
.#.....##.#######..#...#.#.##.#.#...#.....##.#.......##......##.##..#.#.#.##..#.##..##.#.##..##.#..#
###.##..##.###.##..#.#.#.#.#.##......##..##...#.##..##.#.####..###.#...#....##.##.#.#...#.....#.##..
###..#...#..##.##..#.#...######...#.###..###..##.##...#..###.....#...####...#..#...#.##.#.###.......
#...###.#...#####.#.##...#...#.....###..#..#.##.##.###....##.#..#.....#..#.##.#..####.##.....##.#..#
#..##...##..###......#####.##.#.#..##.##.##..#.......#..#.###.#...##..#####.####.#.....#.###..###.##
...#.......#.#..######..####.....##.###..#####..##....#..#.#...#..##.#....###.#..........###.#.#.#..
.###...#.##..#.#...#..##..###.##..#.#.##.#.#..#.#..########..#.#.#...#.##..#...###...##..##..##.####
.#####....##..#.####.#..#..#.###.####....#..#...#.#.##.#..##..#.###.###...#...#....##.....##.#..###.
.#..###.##..###......#.#.##..#########.#.###............##.##......#####.#..#..######..#....#.##.##.
.##.......####..###..###...####..#..#####.####..##.....#.###..#.##..##.#.#....##...#..##....##.#.###
###.###.#..#.##....##.#..#..#..#..####.#.#.##.#.##.#.#####.#..#.#.#####.####.##.#.####.....#.#.#####
##..#.####..##.####.#####..##.#..###..##.##.....####.##..##..#.#..#......##.###.#..########.#.#..#..
####..###.#.######...####.###..#.#....##.#.#.##.#.#.#.##.#....#.####.#.#.#####.......##.#...##.##...
..#..##.#.##.#.....#.#.##.#.#.#####......##.##.##.####....####.#.#.###....##..#..#.#####.##...##.#.#
....##..#..#.#.#.##.##.#.###..#.###.....#.##.#.##.#.###.#....#.....#....#####.....#.##...#.##....###
###.#.##.###..###...#...#...#.....#..##...##.###.#..##..##.#.#.#######.....#..#.#.#.####.#.#...###.#
.##.####.#.##..#.#....###..#.##.#.....##..##.##.....###..##.#...####.##.#.#######.###........#.#.###
......#.##.######.##...##.#..##..#.#####...###.#....###.######.#####...#.#..##..#.##....#..#....#..#
##...#....#..##..##.#.##.#.#...##.##.#...##.##.##..#..#...#...##..####..######..#..#.###...#..#..#..
....#..#...#.#.###....#..#.#.......#..#.###..#######.##.#.####.#..#.#.#..##....#..#.##...#.###.####.
..###..##.#...##.##....####.##..##.##.##.##...###..##.#.#....##.##...##.....##..#.###.#.##..#######.
#.##........##....#.#..#..#..#.#.###..#.##.#.#.###...#.##...#....###..##.#.#..#.###.#..##..#.#...##.
##......#...#.#...###..........#...##.#..######...#.....#.#.##.###.#.#.#.##.###.#....#..#.##.##.#..#
#..#####...#.#..###..#..##.##..##...#.##...#.###.#..#.#..##.###.####.##..##.##...##..#.##.#...#.####
##.###..#.....###.#.#.#..#..##.#........#####.#..#.####.#..##.##..#.##...#.#...#.#.##.##..#.###.###.
#####.#..#.##...#.###..#####...#####..##..#..#..#####..###.####.#...#...####..##.###....##.##.###...
##.####.#..#..##.#..#..###...####.##..#.#..#.##.#.###.#..#.#...#..##.#.#..#######.##.#..##..###...##
##..##.....##..#####..#...###.##.###.####.###.##.#.########...#.#.####..###.##.#..##########.#.....#
#.#.##...#.#...##.##..#.#.#...#.#.##.#.###.#...##...##.....###.#..#.#..####.#..#.#######.##.#.##.##.
##.#..####.#.....#.#..##.##...###...#..#.##.##..###.#####.##....#.#..#...#####...#.##..#.#..#....#..
##.###.##.#...#.##.....##..###..#.#..###..##.###.....#...#...#.##.#....#..#...####.#..#..#.#.#.#.###
.####......###.#........#..#..#....###.#.#.....#..#...###.####.#...###.#..###.#.#...###...###..#####
##.#.###.#.#.#..##.##.###.######...#.#.##..#...##..#...##.#.##..#.#..#.##.#.#.##.##.#..####...#.#...
##.......#.##...#.#.....##..#.#..#...#..#..#..#..#.#.###.##.#.#.#########.#.####...##......######.##
....##.#.##.##.#.#.#.#.##..####....#..###.#..#.##...####.....##.#.....#####.##.......##.##.#..###.#.
.#####..##...###.##.#.....#......#..#.#..#.#..#......##..##.##..#..##.....#...##.#....#..##..#..##.#
#.###..##...###....#.###.#.#.##..#....##...#..#.######....##.#....##...####.###.#####..##......#...#
##..#.#...#####..##.#.###..##..#.#.####..#..#.##.#.#.#..#.##..#.###.#####.##..#...#..#.###..#.##...#
#.#...#######..#.####...##.#.#######..####..#.###...####.####..#...#.#....#..#.##...#.##.#..####.#.#
#...#.##......######.#.####..####.#.#..#.#..#####...##..#.##.###.#..#.####.###.##..#..####..####....
###.###..#.......###..#..#.##...##.###..#...###.#....#...###.#.#.#.#...#....#.##..##.########.##....
.#.....##.....#.#.####......#.#.#..#######.#....#.....###...###.##...#..#..##.###.#...#..###.#.#####
##..#..###.##...#...#...####..###...###.#.#..###.#####...#####..#####..#.#.####.##.#....#.####..####'''

test = '''..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###'''

alg, img = input.split('\n\n')
alg = "".join(alg.split())
img = img.split()
temp = []
for row in img:
    temprow = []
    for char in row:
        temprow.append(char)
    temp.append(temprow)
img = temp


def binarysquare(img, x: int, y: int):
    binarystr = ''
    # opp venstre, opp, opp høyre, venstre, null, høyre, ned venstre, ned, ned høyre
    nbs = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0), (0, 0), (1, 0),
        (-1, 1), (0, 1), (1, 1)
    ]
    for nb in nbs:
        if img[y+nb[1]][x+nb[0]] == '#':
            binarystr += '1'
        else:
            binarystr += '0'
    return binarystr


def binstr_to_char(binstr: str, alg: str):
    ind = int(binstr, base=2)
    return alg[ind]


def printimg(img):
    for row in img:
        for char in row:
            print(char, end='')
        print()


def border(img, char):
    bordered = []
    extra = [char for i in range(len(img[0])+2)]
    bordered.append(extra)
    for row in img:
        bordered.append([char] + row + [char])
    bordered.append(copy.deepcopy(extra))
    return bordered


def enhance(img, alg, borderchar):
    enhanced = border(img, borderchar)

    temp = copy.deepcopy(enhanced)
    for y in range(len(enhanced)):
        for x in range(len(enhanced[0])):
            if y == 0 or y == len(enhanced)-1 or x == 0 or x == len(enhanced[0])-1:
                if borderchar == '#':
                    temp[y][x] = '.'
                else:
                    temp[y][x] = '#'
            else:
                binstr = binarysquare(enhanced, x, y)
                temp[y][x] = binstr_to_char(binstr, alg)

    enhanced = temp
    return enhanced


enhanced = border(img, '.')

try:
    for i in range(1, 501):
        if i % 2:
            borderchar = '.'
        else:
            borderchar = '#'
        enhanced = enhance(enhanced, alg, borderchar)
        print(f'Step {i}')
except:
    printimg(enhanced)
    ans = 0
    for row in enhanced:
        for char in row:
            if char == '#':
                ans += 1

    print(ans)
