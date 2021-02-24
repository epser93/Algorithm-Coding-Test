def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

winProb, loseProb, drawProb = map(float, input().split())

# 승,패,무 횟수 구하기
result = []
for i in range(21):
    for j in range(21 - i):
        z = 20 - i - j
        result.append([i, j, z])

probList = [0] * 5
for resultNum in result:
    win, lose, draw = resultNum[0], resultNum[1], resultNum[2]
    point = 2000 + win * 50 - lose * 50
    prob = (factorial(20) / (factorial(win) * factorial(lose) * factorial(draw))) * (winProb ** win * loseProb ** lose * drawProb ** draw) 
    if point >= 3000:
        idx = 4
    elif point >=2500:
        idx = 3
    elif point >= 2000:
        idx = 2
    elif point >= 1500:
        idx = 1
    else:
        idx = 0
    probList[idx] += prob

for prob in probList:
    print(format(prob, '.8f'))