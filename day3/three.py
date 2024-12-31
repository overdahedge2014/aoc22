import sys
print(sys.path)
# from AOCBoiler import op

# sacks = op("day3/input.txt",'\n')
fd = open("day3/input.txt")
sacks = fd.read().split('\n')

def solve1():
    tot = 0
    
    for i in sacks:    
        str = ""
        first, second = i[:len(i)//2], i[len(i)//2:]
        for j in first:
            if j in second and j not in str: str += j
        for i in str:
            if i.islower():
                tot += (ord(i)-96)
            else: tot += (ord(i)-38)
    print(tot)

def solve2():
    tot = 0
    pos = 0
    done = False
    for i in sacks:
        if(pos % 3 == 0):
            for j in i:
                if j in sacks[pos+1] and j in sacks[pos+2] and done == False:
                    if j.islower():
                        tot += (ord(j)-96)
                    else: tot += (ord(j)-38)
                    done = True
        pos += 1
        done = False
    print(tot)
        


#solve1()
solve2()