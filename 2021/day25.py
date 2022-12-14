import copy

test = '''v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>'''

input = '''.v.v.v>...>vv>v>>>.v>..v>.v.>.>v>.v.v.>>v...>.>....>.>vv>>>.....>>...v.>>v..>..vvv.>v...vv...>..>....>.>.>.>vvv....>..vv>v....>v...>>....v.
>.v>..v.>>vv.>>v...v.>.>..v.>.>.>vvv..>>>.>...>v>.>>v....>>>>...>v.v>.v>....>>>v.>>>....vv.....vvv.v.v..>.>..v>>.>.v>.>v>.vvvv.v..v>>..>>vv
.vv>>...v>..v..v>v.>vvv.v.v>>.....v>>.......>...v>.v>.v.vv.v.>v>v.v......>>......>.v...v........v.v........>.v.vv.>>.v.>>.>.>...v....v>>>..
.>.>v.>vv.v...v.>>v>.>v..vv>..v.v.>...v....>vvvvvv>>>v..vv.v.v>>.>>.>>v>v>>..>.v...v.v.>v..>...v.>.>>.v...v>..v...vv.>v.....vvv.v>.v>..>>v.
..>.....v.>>..>>.v>v.>.>>.>..vv.v>>.>..>.>..v>>...>.>>.vv>>>..>>>>.v.>....>>.>..v>>vv>.>>v>vvvv>vv..v.v.>.v>..v>.vvv>>.v.......>>.>...>>.>.
v...>..>..v>.vv.>>.>...>>....v.......v>...v.vvvvv>..v...>.v.>.>>v>v.>....v>...>...v.>.vv>......vv>.v>vv>>....v>.v>.>..>v.v..>>>.>>>..v..>vv
v>v>.v>..v..v.>..>...>v.>..>.>vvvv...v.v>v....>.>v.vvvv....>...v.v..vvvvvv..v.v..v>v....>v....>v.>>.v>.>v..>...v.vv...>v>>..>.>.....v.v..v.
.......v.....v>v.vv.>.v>.>>.>v.....>>..v.v.v>v>.....v...>v.vv>>.vv>>>>.>>.v.>v>..v.v..>v.vv....>>.vv.>v...>>v....v.v.>.vvvv.v....>v>>>>v.>.
v>.v>..v...vv.>vv.v...v.v>.>........>.vv>>..........v...>vv....>.>v>v..>..>>>v.>>..v.>.>...v.v.>..v>>>..>v.....v.>>>>...v>>v...vv>..>>.v.>>
.v>>>>>>v.>.>...>.>>.>.>>v>.........v..>.v>>>v>.....>...>>.>.v..>.vvv.>..v.v..>.>..>v>v.>v......>>...>>v.vv.....>.>...>.....>v.v..>>v.vvvv.
v......>.......>>..>.v.>..v..>>v..>>......v>v.vvv.>...>>>...v..v>vv.....v.v>v>>v..v.v..v.......v.>v>.v.v..>.>..>v.v>>>v..v.>.>.>>v.>..v.v>.
>.v..>>....>.v.>...>>>..>.v..v>v..>>>.v..v....vv>vv.v.v..v...>>..>......>>..v.....v.v>>.v....v>>....>..>v.vv.>.>..v...v>>.>.>v.v.vv>.v..v.>
..v...>...v..v.v...>...>.v..>...v...vv>..v....v>>>v.v..v.v>v..>v..v..v>>vv.v>..v..v...>.......>..>.>v>v..>...>v.....v..>v>v...v>..>.>...vvv
.vv>.>.v...>>...v.>.>v.v.>>v..v.>v.>>vv.v>.>..>....v.>v>vv>..v>v>v.>>v>v.>...v>vvv..>>.v.>v.>vv.>..v>...>.v..>.>>>v>>...v>.>>v..v....v>v..v
..>.>>>...>........>.vvv>>.>v..v.>v..v..>v.>>.>.v..>.v...v>>.>v..vv...v.v>.vvv...vv>vv>v>.>vv>.>v.vv..v.v...v.>>..v...v>...v..vv..v..>.>>>>
..>.>.>v.v.>.....>vv.vvv>.>..v>>>v.>vv.>.v.>.....v>>.....>v..vvv....v.>.v>.v.vv>v.>vv.v..>v>>...v>v....v>>v>....v..>vvvv>..>v>.v..v.....>..
.vv>.....v>.>>>.>>v>>>v>>>v>.v>>.>v..>>v.vvv...>vv.v.v.v.....>>vv..v.>>>>v.>....v>v.>..>..vv>>>....vv.vvvvv>v....v...>.>.vv...v...>vv...>..
>...v.vv.vv.vvv..>v.>.......v...v.>v.>..>.v>..v...>v..>..>v.v..>.v>.>>.v>.>v...v>>.>v.v.v.v>.>..v.>vv.v>>>.>vv.vvv.>vv>>v>..v>>.vvv>v..v.v>
>v.>...>v.vv..vv>..v.v..>..v.>v>>>..vv...>.>.v.v...>>.>v.vv..>.v.>>.>.>.v>..>.>..v>..v>>.v.v.v>.>...v.v.vv.>>>.v>...v.v>..>>..v.v>vv>vv>>vv
vv.vv>....>..>...>>..v.v..v..v....v.>.vvv>>.v.v>.>.vv.>v......>vv>>.>>.....>>....>..v.v..v.v...>>v.>>>v.....v.>......v>v>v>>.v.vv...>.v....
.>v>....vv.v>>...>>....>>>.>.v>...vv.v.>vv>.....v>v.v....v..v.>v>.....>...>v>>....v.vv.v>>.>..v>.v.v...v..>..>>v.v>....v.>....v>......>v...
..vvvv>.>.>.v.>.vv....>>>v..>..v..v>vvv.>v.>>.>v.>.vv>vv.>......v...vv>v..v.v.vv>v.v..vvv>v..>>...>..>.>....>>v>....v.>vvv>>..>>>..v..v.>..
>.....>>..v>.vv.v>..>..v.>vv>>vv>.v>v..vv......>....>.....>.>v.vv.vvv.v..>.vv..>>...>vvvv>..>..>.>>.>v.vv>...>>vvvv.>.v.v...>...>v>..>v....
.v.>v..>vv.>v...>vv.v..vv>.>>.......>v>.vv..v.vv>v..>.>vv.v>>>.>>v>.>...v...vv.>>>v...>>..v>v>v.v.v>..>.v....>.v.v.>vvv.v.vv.>.v..vv.>>v>>.
....v...vvv>>>.>>.>v>...>.>v.v.>.vv>...v...>>v.v.>.v>..>...vvv....v..vv>vv>>>..>.>.>v....>..v.vv.v..v...>>>v..v.>.....v>>v>vvvv.>.>.v.>vv..
.>.>v..v>.v.v.v>v.>.vv...vv.>.>v>....v>>v..>....>>>.v>v.v>>..>.>vv..>.>..>.>>.........>>>>..>...vvv>.>.v.>v.v>...v.>vv..>.>v.>>vv.>>>v>.vvv
>..>>..>.>>>vvv.>....>>v.>..v>v>v....vv.>.>>>v..v..v>.v....v>>...>>v...vvvv>>>>.>.....v>v.v.v..>v.v..>.v.>v>>....>>>v>.v>v.>.v...>>>.>vv.>>
...>>..>..>.>v.v..vv>.>.>vv.v>>.>....>.v>..>.v>>.....v.v.v.v..>...>>v.>.v.v.>>.>v....>..v..v>>..>>.>.v..>>..>vv..vv>v.v.v..v.vv.vv>....vv..
.v.v>..>.>.v..v>>....v>....>v>>>....>......v..v.......>vvvv.vvv.v..>.>..>.>>v.v..>...>>vv>.v..v.v..>vv>..>>.>v.>.v...vvv>>..>.vv..v.>v.v>v>
v>.>.>.v>>v.>>v>.>.vv>.>>...>..>>>.v....>>>v>.v>v.>.v.>..>vvv>.v.>>....>v....v.vvv>..>.>.vv>>..>>v...vv.>.>>.v..v>.v.>.v..>.v>.v....v...>.>
>vvv>.v>..>>..>.vv>>>...>>v.>v..>v....v>vv.>..>.v.>....vv....v....>....vv.v...vv>>>.>..>>>.v....>>vv.vv>vv>>.v...>>>v.v...v.vv..v>.vv..>v>.
v.>...>>..>>v>..v.vvvv..>>.v>.v.>.vvvvv>v..v.v>....v..>>.>>..v.>.v>..v.>.v.vv>.>.>v.v....>v.vvv>>>.v>>.vvv..v..>.>...>.>..>.>...v..>>v.....
.>v.>>v>..vv.>.vv.>>...v.v....>>>v....vvv>.v.>v.>v.vv.>.....>..>>.vv.v.v.>..v.>...>>.>.....>>.>........v>...>.>>>.>v.>.v.>>.....vvvv.v.>v>.
>..v..>.>>>..>vv..v..>.v.v....v>...v>....>>...>v.>v...v..v...>.v>.>.>.vv...v....>>....vv.v>>....v.v.v....>v.....>.v.v...v>..>>..>..>>..>>v>
.>vvv.v>.>vvv>>vv>v>v..>...>vv.>..v>.....>.vv....>>...>>.>>>v..vv.>>.....>>.v..v.v>>.vv>..v.vvv...>>.>..v.v>.v......v...>.>..>..>v....vv>.v
.>v>...>...v..v>.v..v>v.v.>>.>vvv...v.>..............vv..vvvv>.>....>.>>..v.vv.>>.>.vv>...>>v.>.>.v..v>..v..>v...>.>..v.......>.>v.....>...
..v.>v>vv....v>>.v>vv....>.v>.>v.vvv>vv>>vv>..v>.vvv>.v.>v.>....v.>..v>v........v.>>>v..>>.>v>v...>>vv.>.v.>>.>..>..>vvv>.v.>vvvv.v>v.>v..>
.vv>>v......>...v>.vv>..v>>.v>v>>v>...>.>>.>.>...v...>>>>>vv>.>v....>v..v>>.>.vv>..v>>v>.v..v.v..v>......>.vv>....>v>..v>>.>.>>.v>v>v>>>v..
>v.v>.>...vv.>..>.v.>>.vv....>.....>v.v..v.>..>...>.v>v.......vv.v>.>vvv...>..>.>....>v...>..v...>v.......vv..>....v...>v.....>>v.>vv>.v.v>
v>..vv>.vv.v...vv...>......>v..>>.v>vv.v>>v..>v>..vvvv..>.>>.v..vv>.v>.>......>......>vv.v..vv>>..>..v..>v..>..>...>...>.>.........v.vv>v.v
.v>.>.......>.v.>.v..>>.>.v>...>..vv......v.v...>..v>>v..v..v...>>vv..v.v...v.v...v>vv>..v.>>>v.v.v>v..>vv>..v..>>>>...>.>..>.>>>.>>vv>>..v
.>..vvv.v>.v..>..v>>..v>v>>.>.>..v.>vv>.v.>>v>v.vv.....v.>v.>>>>vv>>>..>>...vv>v..vvvv>>>..v.v.>...v.....>>...>>..>.>.>v..>..>...>..v.v>..>
vv..v>.v....v..v>.......>vv..>vv>...vv...v>>vvv>v...v.>v.v>v.>.v.v.>.>.>....v.>>>..>.v.......vv..v.vv>.v...v...>....vvvv>....>.v..v.>v..v..
>.vvv.>v....vv>>v.>..>.vv.>v>.v.>..>>v......vv>>>vv.v..vv.v.vvvvv>>.>>.>>v...v..v.>..>...>v>.v.v>vv>>.v.vv>>..v.>>>...>>.>v.v.>>..vv>..>.v.
..v.v>..>v>..>.......>>.>>>v..v.>....>.v..v>...>v>v.>.v.>.v...>....vv..>..v.>......v...>vvv>..v..v....v>...v.>.v......v>vv..>.vv...vvv.>vv.
vv......vvvv.>>.>v>.>.v>.vv>v>.vv>....v....v.v.>vv>vv.>>.>.v>v...v.....v.>..>....v.>..>..v.....v.v>>v>.v.>..v>..vv.v.>>...>.vv>....>v.v>>..
v>.>>.>.....vv.>v>>.v>..>v.>..>>.v..v.>.>.>>.vv>..v..vv.>>v..>.>........v....v>>v.v.>v..>.>v......>..>.>.v.>...v>..>v>..v.>v>v..>vv>..v.>>>
v..v..>...>.v..>>...>.>v..>v.v.vv.v..>..v..>.v.>>v.>..v.>..v>..>.>vvv..v.>.>>.v.v..v>.>v.>..>v..v>>v>>......vv.>.>.v.>>v......>v...>v...>>.
.>..>...>...v.....>.....vv.v.>v.>.>..v....v>>...>.>.v..>>>...>v.v..>...>vv>..>v>.v.>>.vvv>>v>v.......v.vv...>>>..v...v.>v..v.>..>vv>..>.v>.
....>vv.>..>.>>.v..>.v.>..v..>..v.>>.>v..vv.v>>>v.....>>...>v>......>.>v>.v.>.vv>.vv>.v.>>..v>..>vv.v..v...>vvvv>>..>..v......v>..v.v.v>.>.
....vv>....v....>...v>..v>.>.>.>v..>.v>.......v>..v.vvv.v.>..v.>v>.>vv.v.>vv>.>>v.v..v.v...>vvv.......>v>v.v..>.v>.v>vvvv.>.>>>.>..vv.>v..>
..>.vvv>.>vvv>>>vv.>..>v.v.vvv>..vv.....>v>>..vv>.....>...>.v>.v>>.>.>vv..v...v..>.>>..>>.>.vv>v>>>vv....v>.>>..>..vv>.>>..>v>.v.v.v..>...v
.>.v>............v>v.v......vvv>.vvv>v.v.>vv..>>....v.>.vv.vv..>..>>>>v.....>.>.>..v.>.>..>.vv.v.v......>>.>>>.>>.v..>v>v...v...v>...vv>.>.
>>.v....v..>..v>>v....>...v.v....v.>..>.v>v.>v>.>>v.....>.v.>>.>>>..>.v.v.>>vv>>.>..>>v...>.>.v.vvv>>vv.vv>.v.>.>.>vv.v..>v>.>.vv>>>v..v>.v
>v..v.v.>..>>>>..>>v.v>.v>..>>....v.....>..>.>v>...>>.v>....vvv>....>v.>.v.>.>v>.>v>>.>v>v..>.....v>.vv..v>>...>>v....>v..v>....>...vvv.v>.
.>.v.....>..>.>vvv.>v.>vv.>..v..v.v.>vv>.>..>.>>>.....>v......>v.>....v..>.>..v>v.>..>.>v..>.v.>v>v>...v.v.>.v.>vvv>vv..>.v..v>..vv..>..v>.
.v>.v>v>.v..v>.v..v.>............>v.>..>..>>.v..v>v>vv>>.>v.>>.v..v...v....>.v..>vv.>.....>.>>.vvv..>>..vv>>v>.....>>.v>...v.vvv>>..>..v.v>
v...>..>...v.>>.v...>..v>v...>vv.v..>vv>..vv>>.v..vv.v>v.>>..v>v.v..>.......v...v.v>...>v.v......v.vv>...v.>..>vv>v.v....v.v.vv.vv.vvvv.>v.
.>.v>>....>....vv..>vv>.>..vv.>>...>....>vv.vv...>.vv>v...>>..v...>..v....>v.vvv...v>>.>>>>>v>..v>>vv>vv.>vv..v...v.vv..v>v.>.v.v>..v..v.>v
.>.v.v...v.....>..v>..v>.vv.v>...vv.....>v..>..>..>v.>.v...>.vv.....>.>.v.v>v....>..>>.vv.>vvvv..>>>.v...v...>v.vv>>.v..>v..>..>>.>..v>v..>
>..vv>>v..>.v>>>v>>.v..vv>....v.>vvvv.>...vv...>.v..>v.>v>.>v>v>>v.>.>...>>>.....v.v....v>...>..>.>v.>.vv.....>.>>vv.....>......>.v..>v>.>.
v.......>>.>..v>.v.>.>v..>>.>.>vv..>v.v...>.v>..v....v..v..>.>>...v..v>.vv.>v>>.>....>vv>.v.v.>..vvv.v.>.v>.v>v..>.>>.>.>..>.>...vvvvv.v>..
>..v.v>.>>v.>>...v.>v.....>.v.>.v>v.>v>.vvv>.>>..>v..v.v.>...>v....>v.v.v>>...>.vv>.>v.vv....v>..v>>v.>.>..v>v..>v>..>.>>.v>.>..>..>..v....
.>vv.>.v>>>.>.>.v>v.>..vv>..>>>.>>...v.....>v.v..>.>.>>.v.>.>v>.>v.v..vvvv>.....v.v..vv....v.>...>.vv.>>v.....>.>vv>...v....>v..>v..vv.>>>v
v..>>>v.>..v>.v.v.>.>..>..>>..vv.vv.>.v.v..>v>v.>>>.>.>>.>>.vvv..>...>>..>.>..vvv>.>..v.>.>.v>v>.>v..>.>.v>....v..>..v.>v.>>.v.v..v>v..>v..
....>v...>....>.v>>vv.....vv>..vv.v....vvv>>...vv.v.v.>......v.v>>v..>.v>..v>v.v..>....>....v.vvvv>v..v>v>v>v.>>v....v.>vv>>v>vv>>>.>..>.v>
...>>>.v.v.....v>vv>>v>.>..v.v>v>....v>>vv..vv>v>..vv...>.>v>.>v..v...>.>vv..v.>.v..v...>...v>...v.vv>vv>..v....>.v....v.v>..>.....v..v..v.
.>vv.v..v>..vv....>.>>>>..>>>>..v....>.>v.vv.v.>>.>vvv..vv..>vv.>>v>>v.v..>.....>>v>..v..>>v>vvvv...>.>v>..v..>v>...>>.>vvv.v.>vv.>..v>>...
>>.>...>v.>vv>v>.>.....>.vv.>.vv>.>>.>.>...........v>.>..>>.>.>>..v.v>>v.vv>v>.>v.>..v>vv>.>>.v>>.>.v>v.v..>v.v>.v>v>>.v.>v.>>vv...vv.vv...
>vv>>.>...>v.>v>...>v>.v.>...vv....vv>v>.>..>.v.v.vv.v.>v......>..>.vv..v>.>>.>v>...v.vv..v...>vv.v.v...>>.>.>.v..v..>.vvvvv>>>>v>vv.v.v...
>v>>>.v>..vvvv..vv>...>.>.v>>>..v.v>>.v..v>.v.....>v>>.v..>..>.....>v....>.>..>......>v>.>.v.>..v..vvv>>v.v..v>..v.v.>>>>>>>vvvv.vv.>vv..v>
..v..vv>v>v...v...>.vvvv.v.....v..>.>..>....v.....v>.>>..v.v.vv..>....vv>vv>v>>.>>v>>.>.vv.>..>>v.v>...v>.v...vv.>v....v.>>...>v.>.vv.>.vv.
.v>v..>vvv.vv>v>>>..v..>v>.vvvv.>.>.vvv>.>..vv.>v...>...>v..>..>......v...>.v..v>>.>v...>>>>.....>>>..>vv.>>>v.>v..v>>vv.>....>..>>vv.>.>..
v.>...>vvv>...>.>.v>.v..v..v>.v.>.v>.v...vvv..>.>>v>...>.>>v>>.v.>v...>>.v.v..vv..vv.>.>v.>.v.>>>.>.vv...v.v>.v.>>>>>>..vvvv..>....>..>.v..
>v..>v....v.v....>vv.>.>.>v>.>v>v.v>>>.>v...>>>.v..v.v.v>v......>vv.v..>......>v>.v>>.vv>>>...vvv.v..>.>.........v.vv>.>vv.vv>v.v.>.>vv..v.
>.v>.v.v>v..vv.v>v>.>>....vv..>.vvv>v..>>>>vv.v>....>.vv.>...>>>...>v>.>...v..v>v...>..v...>.v..v>.v...v.....>vv........>....v>v..v.>..>v..
>...>v......v>.>v...>.v...>>v.v>..>v...v.v..v>.>.v>.>...>vv.v>vvv.>..>..>...v...>>..>.>v.>vv.v..>>.v.v.v..>.v>..v.>..v...>>v.>v>v.v.v.>..>.
..v>.>>v>>..>..vv>>..>.>>vv..>..vv....v.>v>.....>v>..v.v>.v..>...vv..v.>>vvv...v>v>.>.v.>>>.v>...v>.>v.v>v>..>...>....>>>v..v..>>...>.v....
....>...vv.>...vvv>v..>vvv>>..>>>>......>>>.v..v>vv>v>.>....>.....v.v..v.v.....v.v..v.v..v>.>v>v>.>.v.>v>....vv.v..>.vv..>..vv>.>v.>.......
vv.>.>...>vvv.>v.>v>.>.>.v..v>..>.>>.v>.v>.v.v..v>v...v..>>.>>.>.>....v.>..>>vv>....>..>>...>>v.>.v>>..>>...vv.v.v.>>..v.v...v.v>..v.v..vv.
.>v.v..v.v.>.v.....>.v...>.vv>.>....vv.v.v..v>.v>v>>>.v..vv.>vv.v....vv..vv.>>>v>.v.......>.vv.v..>v>v...v...>..>vv....>.>.>.>>v...v..v>>.v
...>v.>>.vv...>v.v.v>...v.>vv..v.v...>>>>..>.....>.>v.v.v>.v.v>.>>.>...vv..v....v>.v.vv..>.v>...>>..v.v.v.v>.v.v>v.>..v.>v..>>..>vv.......v
>....v..>..vv.>.v>..>.>.>.>>v..vv.>vv...>>v.>.vv.v.>.v..>vvv>.v...vvvv>vv.>>>.>>..v.>v>>>..>>.>.v>>>v>>>..v>>.>.v.>...v.....v..>..>>.>v>..v
>..vvvv>>..v>v>......>...v>...>>>...>.v>.>.v>.>>....vv..v>>>vv..>>>v.v>.>.v..>.v>..v>....vv>.>.v.....>v>.>.>.v>v.>.>v>v....v.>...>.v.......
.v...v.....>>v.>vv.>v.>>.>.v>>.v...>>.v..v.vv>>.v...>>>v.>v>>..>>...vv.v>v.>..>v>.>v>>..>>.v...>..>.>..vv.....>>.>.vv>v>>.>..vv>.v.>v.>.v>v
.vv>...v.>.vv.>>...v..>.vv...>.v.....>>..v..>v.>.>...v>..>v.v>.v.>v....>..>..>..>.>.>.>.>..>.>.>.>..v..v>>v.>.v>>.....v..>.v.....v>..v....v
.....v>v..vvvv...v>..>.v.vv.>.>.......v.>..v..vvv.....vvv..>...>.v.>v.>v..>....v>.>>...v>...v>..v>v....v...v.v.>.>v>...v.vv.>...v.>>v>v>..>
>v...>...>..>.v.>>>>.>v.vv>vv>.>.>.......v>>v.>vv...>>.>..v..v>vv..>.>..>v..>v>>>.v>>v.>.>..>...>>..v..v>>v.>vv>>.vvv>..v.>vvv..>..v>vv..vv
..vv.>v...>>........v.....>>..>>..>........>>vv.>.>.....vvv.vvvv>>.>..v.>v>...v.v..vv...v.v..v..>>v...v.>>>>...vvv>>>v>...>vv>v>.vvv..>v..>
..>.........vv.>....v>>.>>vv....>>vv....>..>.>...v..vv.v>..>v>.>v>>.>>>...vv>.......v..v>v>.>.>vvv.>...>.v.>>v>.v>>....v..v........vv.>>.vv
..v.>>v.v..>..>>.v..>.v>>>...>..vv>v.>...>...v.vv>.>.v>..>v.vv.......v...vv>.>vvv.>...>>.v.vv...>..vv..v>...v...>>>....>.>v.>.v...v......vv
>vvv>.vv..>>.>....v..v>>>>v.>.>v....v.v...>>>..v.>..>v..>.vvv..v>.v>.v......>.v.v>>v.v.>.v...>.v.>vv.v>v..>..>>>.>v>>.vvv>>vv>.>v.>..vv.vvv
>>>..>v.v>.vv.v>v>vv...v........v>.>.....v>v..v.>>>.>v..vv..>....vv.v>..v....>>>>vv...>v..v>.v.vv.>..>vv.vv...>>..>>.....vv..v>>..>....vvvv
v>......vv>>.vv..v>v.v>>..v...>.v.>...>>..vv.>...vvvv.>v.>...>v.vvvvv..>>.....>v.>....>....>.>.>v..>.v.vvvvv..v..>vv.v>.v.v...>v.>..v>..>..
.v>>>>..vvv>v.vv>.v>vv..vv.v.vv.>>v>.>..>.v>v....>....v>>>.>.v.vvv.>>...v..>v>...v.v>>v>>v.v...v.v...vvv>>v.>.>...>v..>....>>.>..>.vvv>.v>.
>>.v...>.v>...v>v..v.vv.v..v.v.>...v>v.>.>>.v.>.v>>>.>>.>..>....v..v>>>.v>>.>..>>.>.vv.>>.vv.>>>v>.>>.>.v....v>....>..vvvv....v....v.v.v>vv
>..v>vv>.>v.>.....v.>vvv>..>.>.vv>>>..>.....>..>v>.v...>v..>...v...vv..v>>>v.>>..vv>>..>.>>>v.>..>v...v.v..>.>..>.>>..>.v.v>....>...v...v..
>.>.v...v..vv.>>>vv.vvv..>...vv.vv>...v.v>>>>.>.>>v.>..vv...>v>>v>..>..>vv..vv>>.v>>...>.>v...>..>.>>>.......>.>>.>.>....v.v.............>v
...v>.vv..vv...>v>..>>.v..vv.>.v..v..>..>>.>vvvv.vvv.>>vv>v>.>>v>..>...v>...v...v>>.>..>.>.>v>.v..>>......>v...>v>v.>>.....v>..>.>>>>v.v.>>
.v..vv>....>>...v>.v.v.>.>>....>..v>>.v>v..>......>v...v.>.v......v..>v..>....v.vvv.v..>vv..v.>..v..>>>....>>>>v.>.....v>>.>..v..v>v.v..>..
v>......v..v..v>.....>v>>.>v>v>.>>v>v>v>>...>.....v>.v>...v...v.....>>...v...>.vv..vv..>.>>...>v.>.vv>..v.v>..vv..vvvv.>v..>....v>.>..vv.>>
>.>..v>v..>.vv>>.v>>>>>v>....v.v.>vv..>>...v>v>v.vv>.>>>..>.>v.>>v......>>.>v..v>.vv...vv.v.vv>.>....>.>v...>.v..>.>..vv>..>.vvv.>>>v.v....
>.>.vvv.v>.>vvv...v.>..>.v.>.......>.>....v..>..>...>v..>v....v..>v.v>v.v.>..v.vvvv>>v>.>>.>>>...>..>v>..>v.>v.v..v>>vv.>..v.v>vv...vv>..v.
.v>v.v..>...v>v>.>vvv.>.v.....v.>.>>..v>v>.v.>.>....>.v..v.>v.v>.>.v.vv..v>>v>vv....>>....>vv>v>v>>.v..>.vv..>>>......>>>>..v>v>v>.>>..v..v
..>v.vv..>>v>v.v.......vvvv>vv.v>.v...v>v>>.v>.>.v>..vv...>v.>...v.>v>..v>.vv>....>>..v.>.>vv.vvv.>....v...v>.>..vvv>.>>vvvv>>v....>..>>.>.
.v.v.>vv>.>...v...vv.....v...v>>.>v.>vv>.>>....>>...v.vvv..>>..v.>vvvvv>..v.>....>v.>.......v.>.v.v.>..>>v>vv>>vv.>v.>v>>..>.v>.vv..v..vv.>
...vv.v...vv....>..>..v.>>v>v.>.v...>...v>...v>>v...>v.>>.v...v>>v...>..>v..v>..v..>.v>.>.>..v...vv>v.>.vv>>>..>>>vv.>..vvv..v.>.>..vvv>.v.
.>>.v.>.>..v>..>v>..v>.v.v>>.vvv..vv.>v.>>.>.v.vv.v.vv>.>.vv>.>..v>>.>.v.>v..>>v...v..v>>.>.v>.>.>v..v.v.>>>vv.v.>...v..>v.....>vv..v>.>>>>
.>.....>v>>>>....v..>>>vv...v.>>>v..v>vv>>.>.v.>.>v>.v>v..>..v.v...v..v.>.>>...v.>>v.v>vv.v..>.v>.>>vv...v.v...>>....v.>..vv..vv....v>.....
..v>.>v..v>...v>.>..>...vv>v>vv.>...vv>>..v>.v.>....>....v..>v>.>...v>>vvv....v.v..v>.vv.v.vv.v..>v>>..>...>v>>....v.>>..v.>v.>v.>>v.v.v.v.
.>.v>>>v>.v.vvv...v>....vvvvv>>v.vv>>>>>....>.....>>...vv.>vvv..>.v..vvv.vv>vv>..vv>>vvv...>.>.>.>...vv>.>v.v.v..v>v..v.>.v>>.>vv.>...v.v.>
.>....>>vv.>>>>.>v.>.v..>.>>.vvv>..v..v>..>>.v>.>>>.v.v>>vvv>v...vv.vv..>....>.v..v.>.v>..v....v..vv>v>.>..>..>>>.>>>.v.vvv.v..v......vv.vv
.v.v>>>v.>v.>....>..>.>v.......v>>........vv.v>>>...vvv.>>.>.v.>v.v.>...>v.v.....v.v.>vv>.>>v>>..v>>>..v.v..v......>.v>.>.>>v.v.v.vvv>vv.>.
.>..>....>>.....>.>...v.v....>v>>>v.>.v>.>vv..>v>v>v.>>>>>>v.>>>>>.>.>>.v>......v.v.v.v...>.v..v...>..>>>>>.>.>..>.vv..v>.>..v>.v.v....v.>.
..v>>>>.>>>>....v>v..>>vv.>>..>..v>..vvv>.>..v.>...v>>..>.>>>..vvv.v..>.>.vv>...>vvvv>vv>>>vv..>...>v.>vv....>v.v>..>vv....>v>..v>.v.>v>>v>
.>>.>>>v.>.v>.>.v>.v.>......v...>.v.>..>.vv.>v..v>.v>.v..v...>.vv.v>>.>v.v..>v.>...>>...v.>>v.>>..>v...v.>...v>.>.v..v.>.>....v.>>>>v.>v.>.
>vvv..v.v>>..>..v.>vv.vv>..>vv.v.>...>v..v>>....>>...>>.>>....>...>v>..>>>..>...v.>v.v>.....>..v...>vvv.vv.>>.>v>v.v>v..v>...v..>>.>..v...>
>>.>>...>.>>>..v>>..>v..vv>>>>.v.>>v..vv..>.>..vv.....v.v.v.>..>>>....v.v.>v>>vv....>.....v>v..v>..vv...>..>>v..vv...v.....>vv..v>.>..>.>..
..vv>.v>.....v..>.vv>>...>v...>.v.v>>>........>vvvvv>>.>...>.v.v..v....>.>v>>.v.vv.v..v.vv.>.>v>.>v.>..vv...>>..>.....v...>>>v..v..>.v>>v>.
.vvvv>.>...>>.v..>...vvv>vvv..vv>.>v>.....vv.v..v...v.....>>>v.v>v>>.>v..>>>..>.>v..vv...>vv>.v.>.v..v.>>.....>v.>v>>.vv..v..>..>.>.v....v.
>v>>v...>..>.>>..v..vvv>...>>....>.>>....vv>...>......>..>>v...vv..>>>>>.>v.>.>.vv>>.>>vv....>.v>>..v>>...>v..>...vv..>.>..vvv...>.....>.v.
>..v>.>..vv...v.>>>.v>>.>....v.vv.>..>...>..v..>v.>vv.>..v..>.v.>...vv...v>>..>>vvv...>.>v.>.vv.>v..vv.>>vv.>>..>vv>.v.....>>...v..v.vvv.>>
v.v..vvv>...>v......v....>..>>>.....v>v>>>..v.v..vv.>.>>>>.>.v.>....v.>.>v>vv>vv>v..>.>.v.v>.....>..v>>v...v.....v...v.v.vv>>........v.>.v>
.v>>...>>v>.>...v.>>>....>v>>v.>.v.>>v.v>.>>...>.v.v...vv>v....v>v..>>.>v>.>..>vv.v>>.>..v>>v...>v>>>..v..>v>vv.vv>............>v..>vv.v.vv
>.....>vv.>...v>vvvv>vvv..vvv>.v.>...>v..vv>vv.>>>.v..v>v.>..vv.v.>>v....v...v.....>.v.>.>..>.v>..>v..>>>>>>>v..vv>.v.v>v.v>..>....>>>v>.vv
v.>.v>v.v>...>>>..v>..>>.>..v.v....>.>....v.>..>>>.>v.>.>.>vv..>.>...v.>.....>vv>.>..vv.vvv.>>.vv.>.....vvvv>..v.>.>>v..v..>.>>.>...v>>v..>
v..v>v>..vvv>...v..>.>>...v.v..v..>v..>>.>>.v..>>v...v.vv..v..>...v...v....>v.v.v.v.>.v>vvv.v.v>...>v>.>..>v.v>v>v..v..>>>>...>v.....v.>..v
v>v..v..>..v>.....>>>.v..>v>v..>..>v>...v..>....v...v>>vv.....v.vv...v>....v>..v>>.v.>.>>..>v>..>>>vv.>>>...>...v>vv>v>...>..v.v..>.....>>.
vv..>>v..>>>.>...v..v.>v>..v.>>>>>v..v>v>..>v>>>v.....v..>.>.>>vv.v....v.....>v......>.>vv..vv>.vv..vv...vv.v...>.v..>.>.v>v...v>..vv...>vv
.>...vv>>>.v.....v....>.v......vvvv>.>..>vv>v..vv..>v>>.>v.v>.v>v.vvvvv.v>v......v.>v>vv..>v..>vv.v.v.vvv..>.>.>>v.v.......>vv..v.vv>.>.v..
....v...v.>.v>>>v.>.....>>v>..v>.v.>.v.>..>v.>vv>>vv.>........v..>v>.v>>v>>v.>....>.>...>.>.v.......v....v>vvv..v>..>..v>....v...>.v.>.v...
..vvv.v>.>...>>.vvv>...v...>..>..>...v>v>..>>.vv....>.v.v.>.v>vv.>>v..v>.v.v..v.>.>>.v.....>.v...v>.....v....v.v.v.>>....v.v>>>.......>vv.v
...v>v>..v.v.v...>v>.vvv.vv..>..v.>v.>vv.>.>>..v....>.v.....>.v>..>..v>>vv..vv.>....v>>.v>...>.>vv....v>>.>>v>....>.v.v>v>>>>...>....>.>..v
.>>..v.>v..>>>v.v.v>>...>>v...v>....>.v>>...v.>.v.>...v>>vv.vvv>v....v>.v.>v......v.v.>>.>v...v...>vv.v.....>...>.>..vv.v..>..>.v>..>.v>.vv
>..>.>.>>.v.v.>.v.vvv....>.v>v.v..v.v...>...vv..>>.>..>>>...v>.>.v..v.>>.......v.....>.v>vv.>.v..vv>>>>>>v...vvv..vvv>>>.v.>.v..v.v>v>v>..>
v..>.v.vv>>vvvvv.....v>>v...vv....v>.>>v.v.>.>>v.vv....vv..v.>>.v.v.>v>....>....v.v>>>.>v.v.>v>v.v.v..>.>v>v......v.v>...>v.vvv...v>...vv..
>>vv.....v...v......>v.v..v>..v.v>..>>>.>>..>v>.v>>>.>v..>>>>v.>..vvvv.v>...v..vv.>.>v....>v.>>.....v>v....v..>.>.v>v.>.>.>v.v..>v.........'''

lines = input.split('\n')
seabed = []
for line in lines:
    searow = []
    for char in line:
        searow.append(char)
    seabed.append(searow)

i = 0
while True:
    initial = copy.deepcopy(seabed)
    temp = copy.deepcopy(seabed)
    for y, row in enumerate(seabed):
        for x, char in enumerate(row):
            if char == '>' and seabed[y][(x+1) % len(row)] == '.':
                temp[y][x] = '.'
                temp[y][(x+1) % len(row)] = '>'

    seabed = temp
    temp = copy.deepcopy(seabed)

    for y, row in enumerate(seabed):
        for x, char in enumerate(row):
            if char == 'v' and seabed[(y+1) % len(seabed)][x] == '.':
                temp[y][x] = '.'
                temp[(y+1) % len(seabed)][x] = 'v'

    seabed = temp
    if seabed == initial:
        break

    i += 1
    print('After step', i+1)
    for row in seabed:
        print("".join(row))
    print()
