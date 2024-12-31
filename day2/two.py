

fd = open("day2/input.txt")
txt = fd.read().rstrip().split('\n')

def solve1():
    score = 0
    draws = ["A X", "B Y", "C Z"]
    wins = ["A Y", "B Z", "C X"]
    for i in txt:
        j = i.split(' ')
        if j[1] == 'X': score += 1
        elif j[1] == 'Y': score += 2
        else: score += 3
        if i in draws: score += 3
        elif i in wins: score += 6
    print(score)

def solve2():
    score = 0
    ones = ["A Y", "B X", "C Z"]
    twos = ["B Y", "C X", "A Z"]
    threes = ["C Y", "A X", "B Z"]
    for i in txt:
        j = i.split(' ')
        if j[1] == 'Y': score += 3
        elif j[1] == 'Z': score += 6
        if i in ones: score += 1
        elif i in twos: score += 2
        else: score += 3
    print(score)

#solve1()
solve2()