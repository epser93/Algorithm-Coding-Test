N = int(input())
doughPrice, topingPrice = map(int, input().split())
doughCal = int(input())
topingCals = sorted([int(input()) for _ in range(N)], reverse=True)
calorie = doughCal
price = doughPrice
result = calorie / price
for topingCal in topingCals:
    calorie += topingCal
    price += topingPrice
    tempResult = calorie / price
    if tempResult > result:
        result = tempResult
    else:
        break
print(int(result))