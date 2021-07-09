import sys
input = sys.stdin.readline

A = int(input())
T = int(input())
start = int(input())
cnt = 1
idx = 0
bbundaegiArrDefault = [0, 1, 0, 1]
bbundaegiArr = [[0, 1, 0, 1, 0, 0, 1, 1]]
bbun = 0
daegi = 0
breakFlag = False
while 1:
    for bbunOrDaegi in bbundaegiArr[cnt-1]:
        if bbunOrDaegi:
            daegi += 1
        else:
            bbun += 1
        idx += 1
        if start:
            if daegi == T:
                breakFlag = True
                break
        else:
            if bbun == T:
                breakFlag = True
                break
    if breakFlag:
        break
    cnt += 1
    bbundaegiArr.append(bbundaegiArrDefault + [0] * (cnt+1) + [1] * (cnt+1))

print((idx-1) % A)
