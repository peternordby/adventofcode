with open(__file__.replace('py', 'txt')) as f:
    puzzle = f.readlines()

total = 0
for line in puzzle:
    a, b = line.split(',')
    a1, a2 = a.split('-')
    b1, b2 = b.split('-')
    a1, a2, b1, b2 = int(a1), int(a2), int(b1), int(b2)

    if a1 <= b1 <= a2 or b1 <= a1 <= b2 or b1 <= a2 <= b2 or a1 <= b2 <= a2:
        total += 1

print(total)