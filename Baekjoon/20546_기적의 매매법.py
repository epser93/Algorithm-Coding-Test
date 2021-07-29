def getBNP(money, stock):
    stockCnt = 0
    for todayStock in stock:
        if money >= todayStock:
            cnt = money // todayStock
            stockCnt += cnt
            money -= (cnt * todayStock)
    return stock[-1] * stockCnt + money

def getTiming(money, stock):
    stockCnt = 0
    for i in range(3, 14):
        if stock[i-1] > stock[i-2] > stock[i-3] and stockCnt:
            money += (stockCnt * stock[i])
            stockCnt = 0
        if stock[i-1] < stock[i-2] < stock[i-3] and stock[i] <= money:
            cnt = money // stock[i]
            stockCnt += cnt
            money -= (cnt * stock[i])
    return money + (stockCnt * stock[-1])

money = int(input())
stock = list(map(int, input().split()))
bnp = getBNP(money, stock)
timing = getTiming(money, stock)
if bnp > timing:
    print('BNP')
elif timing > bnp:
    print("TIMING")
else:
    print("SAMESAME")