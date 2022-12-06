input = "8,0,17,4,1,12"
test = "0,3,6"
input = input.split(',')

last = {}

for i, num in enumerate(input):
    if num in last:
        last[int(num)].append(i)
    else:
        last[int(num)] = [i]
    input[i] = int(num)

def findnext(input, last):
    prev = input[-1]
    if len(last[prev]) > 1:
        next = last[prev][-1] - last[prev][-2]
        if next in last:
            last[next].append(len(input))
        else:
            last[next] = [len(input)]
        input.append(next)
    else:
        if 0 in last:
            last[0].append(len(input))
        else:
            last[0] = [len(input)]
        input.append(0)
    return input, last

for i in range(30000000):
    input, last = findnext(input, last)

print(input[30000000-1])
    