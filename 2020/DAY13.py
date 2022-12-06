input = """1001938
41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,431,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,19,x,x,x,x,x,x,x,x,x,x,x,863,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29"""

test = """1789,37,47,1889"""

import math

estimate, buses = input.split()

estimate = int(estimate)
min = math.inf
firstbus = None
for bus in buses.split(','):
    if bus == "x":
        continue
    if int(bus) - estimate%int(bus) < min:
        min = int(bus) - estimate%int(bus)
        firstbus = bus

print(firstbus, min, int(firstbus) * int(min))


skipby = []

for a, bus in enumerate(test.split(',')):
    if bus != "x":
        skipby.append((a, bus))

print(skipby)

found = False
i = 100000
while not found:
    skip = False
    for bus in skipby:
        if skip:
            break
        num = i*int(bus[1]) - int(bus[0])
        print(num)
        for x in skipby:
            z = num%int(x[1])
            if z != 0:
                skip = True
                break
    if skip:
        i += 1
        continue
    else:
        found = True
    
print("We found it at:", i)