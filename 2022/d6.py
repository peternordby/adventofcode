with open(__file__.replace('py', 'txt')) as f:
    puzzle = f.read()

i = 0
finished = False
seq = ''
while i < len(puzzle) and not finished:
    seq += puzzle[i]
    seq = seq[-14:]
    if len(set(seq)) == 14:
        finished = True
        break
    
    i += 1

print(i)