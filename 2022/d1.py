with open(__file__.replace('py', 'txt')) as f:
    puzzle = f.readlines()

calories = []
for line in puzzle:
    calories.append(sum([int(x) for x in line.split()]))

print(sorted(calories))

print(69921+70450+ 72718)