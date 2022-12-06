with open(__file__.replace('py', 'txt'), 'r') as f:
    puzzle = f.readlines()

total = 0
i = 0
while i < len(puzzle):
    one, two, three = puzzle[i].strip(), puzzle[i+1].strip(), puzzle[i+2].strip()

    character = ''.join(list(set(one).intersection(set(two)).intersection(set(three))))

    print(one, two, three, character)
    
    if character.isupper():
        total += ord(character) - (65 - 27)
    else:
        total += ord(character) - (97 - 1)

    i+=3

print(ord('a'), ord('A'))
print(total)