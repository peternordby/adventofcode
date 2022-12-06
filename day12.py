input = '''XW-ed
cc-tk
eq-ed
ns-eq
cc-ed
LA-kl
II-tk
LA-end
end-II
SQ-kl
cc-kl
XW-eq
ed-LA
XW-tk
cc-II
tk-LA
eq-II
SQ-start
LA-start
XW-end
ed-tk
eq-JR
start-kl
ed-II
SQ-tk'''

test = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end'''

paths = input.split('\n')


class Cave():
    def __init__(self, name) -> None:
        self.name = name
        self.paths = []
        if name == name.upper():
            self.size = 'BIG'
        else:
            self.size = 'small'
        self.visited = 0

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    def add_path(self, cave):
        self.paths.append(cave)
        self.paths.sort(key=lambda cave: cave.name)

    def visit(self):
        self.visited += 1

    def devisit(self):
        self.visited -= 1


path_caves = {}
caves = []
for path in paths:
    a, b = path.split('-')
    if a not in path_caves:
        path_caves[a] = Cave(a)
    if b not in path_caves:
        path_caves[b] = Cave(b)
    path_caves[a].add_path(path_caves[b])
    path_caves[b].add_path(path_caves[a])

start = path_caves['start']
end = path_caves['end']
visited = set()
path = []
paths = 0
small_visit = False


def can_visit(cave: Cave):
    global small_visit
    if cave.name == 'start' or cave.name == 'end':
        if cave.visited == 0:
            return True
        else:
            return False
    if cave.size == 'small':
        if cave.visited == 0:
            return True
        elif cave.visited == 1 and not small_visit:
            small_visit = True
            return True
        else:
            return False
    elif cave.size == 'BIG':
        return True


def find_paths(start: Cave, end: Cave, visited: set, path: list):
    global small_visit
    start.visit()
    path.append(start)

    if start == end:
        # print(path)
        global paths
        paths += 1
    else:
        for cave in path_caves[start.name].paths:
            if can_visit(cave):
                find_paths(cave, end, visited, path)

    start.devisit()
    small_visit = False
    path.pop()
    for cave in path:
        if cave.name == cave.name.lower() and path.count(cave) == 2:
            small_visit = True


find_paths(start, end, visited, path)
print(paths)

# 48 min del 1
# ca 30 min del 2

""" for cave in path_caves.values():
    print(cave.name.ljust(5) + ':', cave.paths) """
