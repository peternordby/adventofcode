with open(__file__.replace('py', 'txt')) as f:
    puzzle = f.readlines()

i = 0
dirs = {
    '/': 0
}
path = ''

while i < len(puzzle):
    line = puzzle[i]

    cmd = line.split()[1]

    if cmd == 'cd':
        arg = line.split()[2]

        if arg == '/':
            path = '/'

        elif arg == '..':
            if path.count('/') == 1:
                dirs['/'] += dirs[path]
                path = '/'
            else:
                old_path = path
                path = path.split('/')
                path.pop()
                path = '/'.join(path)
                if path != '':
                    dirs[path] += dirs[old_path]

        else:
            if path == '/':
                path = path + arg
            else:
                path = path + '/' + arg

            dirs[path] = 0

    
    if cmd == 'ls':
        while i+1 < len(puzzle) and puzzle[i+1].split()[0] != '$':
            line = puzzle[i+1]
            
            if line.split()[0] != 'dir':
                dirs[path] += int(line.split()[0])

            i += 1
    i += 1

while len(path) > 0:
    if path.count('/') == 1:
        dirs['/'] += dirs[path]
        break
    else:
        old_path = path
        path = path.split('/')
        path.pop()
        path = '/'.join(path)
        if path != '':
            dirs[path] += dirs[old_path]

free_space = 70000000 - dirs['/']
space_needed = 30000000 - free_space
print('Space needed:', space_needed)
directory = 10000000000000000000000
for key, value in dirs.items():
    print(value >= space_needed, value, key)
    if value > space_needed:
        directory = min(value, directory)      

print('Space needed:', space_needed)
print(directory)