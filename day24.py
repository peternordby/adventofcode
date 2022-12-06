import math
import time

myinput = '''inp w
mul x 0
add x z
mod x 26
div z 1
add x 13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 0
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 11
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 3
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 8
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -5
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 5
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 13
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 10
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 9
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 1
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -8
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 1
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 2
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x 0
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 7
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -5
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 5
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -9
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 8
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -1
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 15
mul y x
add z y'''


class ALU():
    def __init__(self, w: int, x: int, y: int, z: int) -> None:
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    def get_val(self, a: str):
        match a:
            case 'w':
                return self.w
            case 'x':
                return self.x
            case 'y':
                return self.y
            case 'z':
                return self.z

    def set_val(self, a: str, val: int):
        match a:
            case 'w':
                self.w = val
            case 'x':
                self.x = val
            case 'y':
                self.y = val
            case 'z':
                self.z = val

    def inp(self, a: str, val: int):
        self.set_val(a, val)

    def add(self, a: str, b: str):
        if b.isnumeric() or '-' in b:
            self.set_val(a, self.get_val(a) + int(b))
        else:
            self.set_val(a, self.get_val(a) + self.get_val(b))

    def mul(self, a: str, b: str):
        if b.isnumeric() or '-' in b:
            self.set_val(a, self.get_val(a) * int(b))
        else:
            self.set_val(a, self.get_val(a) * self.get_val(b))

    def div(self, a: str, b: str):
        if b.isnumeric() or '-' in b:
            self.set_val(a, self.get_val(a) // int(b))
        else:
            self.set_val(a, self.get_val(a) // self.get_val(b))

    def mod(self, a: str, b: str):
        if b.isnumeric() or '-' in b:
            self.set_val(a, self.get_val(a) % int(b))
        else:
            self.set_val(a, self.get_val(a) % self.get_val(b))

    def eql(self, a: str, b: str):
        if b.isnumeric() or '-' in b:
            if self.get_val(a) == int(b):
                self.set_val(a, 1)
            else:
                self.set_val(a, 0)
        else:
            if self.get_val(a) == self.get_val(b):
                self.set_val(a, 1)
            else:
                self.set_val(a, 0)


def monad(model):
    alu = ALU(0, 0, 0, 0)
    i = 0
    for line in myinput.split('\n'):
        try:
            op, a, b = line.split()
            match op:
                case 'add':
                    alu.add(a, b)
                case 'mul':
                    alu.mul(a, b)
                case 'div':
                    alu.div(a, b)
                case 'mod':
                    alu.mod(a, b)
                case 'eql':
                    alu.eql(a, b)
        except ValueError:
            op, a = line.split()
            val = int(model[i])
            i += 1
            alu.inp(a, val)
    return alu.z


start = time.time()
for i in range(99999992518515, 11111111111110, -1):
    # for i in range(11111111111111, 11111111111110, -1):
    model = str(i)
    if '0' in model:
        continue
    z = monad(model)
    if len(str(z)) < 7:
        print(model, z)
    if z == 0:
        break

print('Found model number in', time.time() - start, 'seconds')
print(model)
