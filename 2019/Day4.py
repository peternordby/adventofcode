legalpasses = []
172851, 675870
for pw in range(172851, 675870):
    if int(str(pw)[0]) <= int(str(pw)[1]) <= int(str(pw)[2]) <= int(str(pw)[3]) <= int(str(pw)[4]) <= int(str(pw)[5]):
        pd = []
        for x in range(6):
            pd.append(int(str(pw)[x]))
        for i in range(10):
            if pd.count(i) == 2:
                pos = pd.index(i)
                if pd[pos] == pd[pos+1] or pd[pos] == pd[pos-1]:
                    legalpasses.append(pw)
        else: continue
    else: continue

legalpasses = set(legalpasses)
print(legalpasses)
print(len(legalpasses))
