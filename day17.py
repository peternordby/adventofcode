input = 'target area: x=241..275, y=-75..-49'


def fire(x, y):
    maxy = 0
    initx, inity = x, y
    posx, posy = 0, 0
    for i in range(10000000):
        posx += x
        posy += y
        if x:
            x -= 1
        y -= 1

        if posy > maxy:
            maxy = posy

        # Check target area
        if 241 <= posx <= 275 and -75 <= posy <= -49:
            #print(i, posx, posy, initx, inity)
            return 1

        if posy < -75 or posx > 275:
            return 0
    return 0


total = 0
for y in range(-76, 100):
    for x in range(276):
        r = fire(x, y)
        if r:
            total += 1
            # print(f'Unique path #{total}')
print(total)

# ca 1 time del 1 og del 2
