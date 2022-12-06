with open(__file__.replace('py', 'txt')) as f:
    puzzle = f.readlines()

m_win = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
}

m_lose = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y',
}

points = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

translate = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}

total = 0
for line in puzzle:
    o, m = line.split()
    
    if m == 'X':
        me = m_lose[o]
        total += points[me]

    if m == 'Y':
        total += points[translate[o]] + 3

    if m == 'Z':
        me = m_win[o]
        total += points[me] + 6 

print(total)
    