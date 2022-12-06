import time
""" i = 1
rolls = 0
while score1 < 21 and score2 < 21:
    diceroll1 = 0
    diceroll2 = 0
    if i == 101:
        i = 1

    for j in range(3):
        #print('player 1:', i)
        diceroll1 += i
        i += 1

    player1 = player1 + diceroll1
    while player1 > 10:
        player1 -= 10

    score1 += player1

    if score1 >= 1000:
        rolls += 3
        break

    for j in range(3):
        #print('player 2:', i)
        diceroll2 += i
        i += 1

    player2 = player2 + diceroll2
    while player2 > 10:
        player2 -= 10

    score2 += player2

    rolls += 6

print(score1, score2, min(score1, score2)*rolls)
 """


def new_pos(p, d):
    p += d
    if p > 10:
        p -= 10
    return p


def universe(p1, p2, s1, s2, universes, to_win):
    # Check if computed solution before
    if (p1, p2, s1, s2) in universes:
        return universes[(p1, p2, s1, s2)]

    permutations = {
        3: 1,   # 1 way of making 3: 111
        4: 3,   # 3 ways of making 4: 112, 121, 211
        5: 6,   # 6 ways of making 5: 113, 131, 311, 122, 212, 221
        6: 7,   # 7 ways of making 6: 123, 132, 213, 231, 321, 312, 222
        7: 6,   # 6 ways of making 7: 133, 313, 331, 223, 232, 322
        8: 3,   # 3 ways of making 8: 233, 323, 332
        9: 1,   # 1 way of making 9: 333
    }

    # Number of wins for each player
    w1 = 0
    w2 = 0
    # Possible moves for p1
    for a in range(3, 10):
        n1 = new_pos(p1, a)
        if s1 + n1 >= to_win:
            w1 += permutations[a]
        else:
            # Possible moves for p2
            for b in range(3, 10):
                n2 = new_pos(p2, b)
                if s2 + n2 >= to_win:
                    w2 += permutations[b] * permutations[a]
                else:
                    r1, r2 = universe(n1, n2, s1+n1, s2+n2, universes, to_win)
                    w1 += (r1 * permutations[a] * permutations[b])
                    w2 += (r2 * permutations[b] * permutations[a])

    universes[(p1, p2, s1, s2)] = (w1, w2)
    return (w1, w2)


player1 = 4  # 4
player2 = 8  # 6
score1 = 0
score2 = 0
to_win = 21

universes = {}

start = time.time()
w1, w2 = universe(player1, player2, score1, score2, universes, to_win)
print(f'\nPlayer 1: {w1} wins\nPlayer 2: {w2} wins\nMost wins: {max(w1, w2)}')
print(f'\nDone in {time.time()-start} seconds!')
