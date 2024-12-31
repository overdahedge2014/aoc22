import re

inp = open("day4/input.txt")
txt = inp.read().split('\n')

def solve1():
    tot = 0
    for i in txt:
        k = re.findall(r'\d+', i)
        j = []
        for l in k: j.append(int(l))
        if j[0] >= j[2] and j[0] <= j[3] and j[1] >= j[2] and j[1] <= j[3]:
            tot += 1
        elif j[2] >= j[0] and j[2] <= j[1] and j[3] >= j[0] and j[3] <= j[1]:
            tot += 1
    print(tot)

def solve2():
    tot = 0
    for i in txt:
        j = re.findall(r'\d+', i)
        k = []
        for l in j: k.append(int(l))
        if k[0] >= k[2] and k[0] <= k[3] or k[1] >= k[2] and k[1] <= k[3]:
            tot += 1
        elif k[2] >= k[0] and k[2] <= k[1] or k[3] >= k[0] and k[3] <= k[1]:
            tot += 1
    print(tot)


solve1()
solve2()