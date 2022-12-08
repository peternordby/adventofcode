with open(__file__.replace('py', 'txt')) as f:
    puzzle = f.read().strip().split()

""" visible_trees = set() """


max_view = 0

for a, x in enumerate(puzzle):
    for b, y in enumerate(x):
        #up
        up = 0
        i = a - 1

        while i >= 0:
            if puzzle[i][b] >= y:
                up += 1
                break
            i -= 1
            up += 1

        #down
        down = 0
        i = a + 1

        while i < len(puzzle):
            if puzzle[i][b] >= y:
                down += 1
                break
            i += 1
            down += 1


        #left
        left = 0
        i = b - 1

        while i >= 0:
            if puzzle[a][i] >= y:
                left += 1
                break
            i -= 1
            left += 1
            

        #right
        right = 0
        i = b + 1

        while i < len(puzzle[0]):
            if puzzle[a][i] >= y:
                right += 1
                break
            i += 1
            right += 1

        view = up * down * left * right
        if a==2 and b == 3:
            print(up, down, left, right)
        max_view = max(max_view, view)

print(max_view)
            

""" visible = len(visible_trees)

print(visible_trees)
print(visible) """