import time

input = '''1,2,4,5,5,5,2,1,3,1,4,3,2,1,5,5,1,2,3,4,4,1,2,3,2,1,4,4,1,5,5,1,3,4,4,4,1,2,2,5,1,5,5,3,2,3,1,1,3,5,1,1,2,4,2,3,1,1,2,1,3,1,2,1,1,2,1,2,2,1,1,1,1,5,4,5,2,1,3,2,4,1,1,3,4,1,4,1,5,1,4,1,5,3,2,3,2,2,4,4,3,3,4,3,4,4,3,4,5,1,2,5,2,1,5,5,1,3,4,2,2,4,2,2,1,3,2,5,5,1,3,3,4,3,5,3,5,5,4,5,1,1,4,1,4,5,1,1,1,4,1,1,4,2,1,4,1,3,4,4,3,1,2,2,4,3,3,2,2,2,3,5,5,2,3,1,5,1,1,1,1,3,1,4,1,4,1,2,5,3,2,4,4,1,3,1,1,1,3,4,4,1,1,2,1,4,3,4,2,2,3,2,4,3,1,5,1,3,1,4,5,5,3,5,1,3,5,5,4,2,3,2,4,1,3,2,2,2,1,3,4,2,5,2,5,3,5,5,1,1,1,2,2,3,1,4,4,4,5,4,5,5,1,4,5,5,4,1,1,5,3,3,1,4,1,3,1,1,4,1,5,2,3,2,3,1,2,2,2,1,1,5,1,4,5,2,4,2,2,3'''
test = '''3,4,3,1,2'''
fish = [int(i) for i in input.split(',')]
days = 256

cycle = {}
for i in range(9):
    cycle[i] = fish.count(i)

start = time.time()
for day in range(days):
    temp = {}
    for i in range(9):
        if i == 8:
            temp[i] = cycle[0]
            temp[6] += cycle[0]
        else:
            temp[i] = cycle[i+1]
    cycle = temp.copy()

total = 0
for num in cycle.values():
    total += num

print(f'\n{total = }')
print("{:2f}".format(time.time() - start), 'seconds')