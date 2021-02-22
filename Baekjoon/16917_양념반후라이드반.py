seasoning, fried, half, minAmountOfSeasoning, minAmountOfFried = map(int, input().split())
result = []

# 반반 없이 양념, 후라이드만
price = seasoning * minAmountOfSeasoning + fried * minAmountOfFried
result.append(seasoning * minAmountOfSeasoning + fried * minAmountOfFried)

# 반반으로만 모두
price = 2 * half * max(minAmountOfFried, minAmountOfSeasoning)
result.append(price)

# 양념, 후라이드중 수량이 적은만큼만 반반으로 채우고 나머지는 오리지널로 채우기
remain = abs(minAmountOfFried - minAmountOfSeasoning)
if minAmountOfFried < minAmountOfSeasoning:
    price = 2 * half * min(minAmountOfFried, minAmountOfSeasoning) + remain * seasoning
else:
    price = 2 * half * min(minAmountOfSeasoning, minAmountOfFried) + remain * fried
result.append(price)

print(min(result))