fd = open("input.txt")
txt = fd.read()

def solve1():
    tot = 0
    max = 0
    elves = txt.split("\n\n")
    for i in elves:
        cals = i.split("\n")
        for j in cals:
            tot += int(j)
        if tot > max: max = tot
        tot = 0
    print(max)

def solve2():
    tot = 0
    first = 0
    second = 0
    third = 0
    elves = txt.split("\n\n")
    for i in elves:
        cals = i.split("\n")
        for j in cals:
            tot += int(j)
        if tot > first: first = tot
        elif tot > second: second = tot
        elif tot > third: third = tot
        tot = 0
    print(first + second + third)

solve2()