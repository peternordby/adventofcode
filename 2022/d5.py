with open(__file__.replace('py', 'txt')) as f:
    puzzle = f.readlines()

crates = {
    1: ['H', 'T', 'Z', 'D'],
    2: ['Q','R','W','T','G','C','S'],
    3: ['P','B','F','Q','N','R','C','H'],
    4: ['L','C','N','F','H','Z'],
    5: ['G','L','F','Q','S'],
    6: ['V','P','W','Z','B','R','C','S'],
    7: ['Z','F','J'],
    8: ['D','L','V','X','R','H','Q'],
    9: ['B','H','G','N','F','Z','L','D'],
 }

for line in puzzle.splitlines():
    _, num, _, start, _, end = line.split()
    num, start, end = int(num), int(start), int(end)
    temp = []
    for i in range(num):
        temp.append(crates[start].pop())

    for i in range(num):
        crates[end].append(temp.pop())

result = ''
for crate in crates:
    result += crates[crate].pop()
print(result)