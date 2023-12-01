TEST = 0

def read_input():
    filename = f"{__file__.split('.')[0]}{['', 'x1', 'x2'][TEST]}.txt"
    with open(filename) as f:
        puzzle = f.readlines()
    return puzzle

def part1(puzzle):
    pass

def part2(puzzle):
    pass

if __name__ == '__main__':
    puzzle = read_input()
    print(part1(puzzle))
    print(part2(puzzle))