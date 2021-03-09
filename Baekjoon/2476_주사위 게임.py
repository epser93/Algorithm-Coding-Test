import sys

input = sys.stdin.readline

N = int(input())
dices = [[x for x in map(int,input().split())] for _ in range(N)]
maxPrice = float("-inf")

for dice in dices:
    dic = {}
    for num in dice:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1

    breakFlag =False
    for num, cnt in dic.items():
        if cnt == 3:
            price = 10000 + num * 1000
            breakFlag = True
            break
        elif cnt == 2:
            price = 1000 + num * 100
            breakFlag = True
            break
    
    if breakFlag == False:
        price = max(dice) * 100
    
    if price > maxPrice:
        maxPrice = price

print(maxPrice)