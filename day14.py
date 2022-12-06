input = '''SHPPPVOFPBFCHHBKBNCV

HK -> C
SP -> H
VH -> K
KS -> B
BC -> S
PS -> K
PN -> S
NC -> F
CV -> B
SH -> K
SK -> H
KK -> O
HO -> V
HP -> C
HB -> S
NB -> N
HC -> K
SB -> O
SN -> C
BP -> H
FC -> V
CF -> C
FB -> F
VP -> S
PO -> N
HN -> N
BS -> O
NF -> H
BH -> O
NK -> B
KC -> B
OS -> S
BB -> S
SV -> K
CH -> B
OB -> K
FV -> B
CP -> V
FP -> C
VC -> K
FS -> S
SS -> F
VK -> C
SF -> B
VS -> B
CC -> P
SC -> S
HS -> K
CN -> C
BN -> N
BK -> B
FN -> H
OK -> S
FO -> S
VB -> C
FH -> S
KN -> K
CK -> B
KV -> P
NP -> P
CB -> N
KB -> C
FK -> K
BO -> O
OV -> B
OC -> B
NO -> F
VF -> V
VO -> B
FF -> K
PP -> O
VV -> K
PC -> N
OF -> S
PV -> P
PB -> C
KO -> V
BF -> N
OO -> K
NV -> P
PK -> V
BV -> C
HH -> K
PH -> S
OH -> B
HF -> S
NH -> H
NN -> K
KF -> H
ON -> N
PF -> H
CS -> H
CO -> O
SO -> K
HV -> N
NS -> N
KP -> S
OP -> N
KH -> P
VN -> H'''

test = '''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''

template, pairs = input.split('\n\n')
pairs = pairs.split('\n')

subs = {}
for pair in pairs:
    combo, value = pair.split(' -> ')
    subs[combo] = value

my_pairs = {}
for i in range(len(template)-1):
    pair = template[i] + template[i+1]
    if pair in my_pairs:
        my_pairs[pair] += 1
    else:
        my_pairs[pair] = 1

letters = {}
for char in template:
    if char in letters:
        letters[char] += 1
    else:
        letters[char] = 1


def sub_pairs():
    global my_pairs
    temp = my_pairs.copy()
    for pair in my_pairs:
        if pair in subs and temp[pair] != 0:
            new = subs[pair]
            pair1 = pair[0] + new
            pair2 = new + pair[1]
            if pair1 in temp:
                temp[pair1] += my_pairs[pair]
            else:
                temp[pair1] = my_pairs[pair]
            if pair2 in temp:
                temp[pair2] += my_pairs[pair]
            else:
                temp[pair2] = my_pairs[pair]
            if new in letters:
                letters[new] += my_pairs[pair]
            else:
                letters[new] = my_pairs[pair]
            if pair1 != pair2:
                temp[pair] -= my_pairs[pair]
    my_pairs = temp


steps = 40
for step in range(steps):
    print('letters before:', letters)
    print('pairs before:', my_pairs)
    sub_pairs()
    #print(f'After {step+1} steps: {template}')
    print('step:', step+1)
    print('letters:', letters)
    print('pairs:', my_pairs, '\n')

max_key = max(letters.values())
min_key = min(letters.values())

print(max_key-min_key)

# Del 1: 15 min
# Del 2: 1 time