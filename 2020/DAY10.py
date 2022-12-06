input = """114
51
122
26
121
90
20
113
8
138
57
44
135
76
134
15
21
119
52
118
107
99
73
72
106
41
129
83
19
66
132
56
32
79
27
115
112
58
102
64
50
2
39
3
77
85
103
140
28
133
78
34
13
61
25
35
89
40
7
24
33
96
108
71
11
128
92
111
55
80
91
31
70
101
14
18
12
4
84
125
120
100
65
86
93
67
139
1
47
38"""

test = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

adapters = test.split()
adapterint = []
for adapter in adapters:
    adapterint.append(int(adapter))

adapterint.sort()

onediff = 1
threediff = 1

for i in range(len(adapterint)-1):
    if adapterint[i] == adapterint[i+1] - 1 or adapterint[i] == 1:
        onediff += 1
    elif adapterint[i] == adapterint[i+1] - 2:
        continue
    elif adapterint[i] == adapterint[i+1] - 3 or adapterint[i] == 1:
        threediff += 1

#print(onediff, threediff, onediff * threediff)

adapterint = [0] + adapterint

builtin = adapterint[-1]+3
highest = adapterint[-1]

def findvalidnext(i, num, list):
    valids = 0
    while i < len(adapterint)-1:
        if list[i+1] <= num+3:
            a = findvalidnext(i+1, list[i+1], list)
            if a != None:
                valids += a
            else:
                return 1
        else:
            break
        i += 1
    return valids

print(findvalidnext(0, 0, adapterint))