N = int(input())
pillars = [list(map(int, input().split())) for _ in range(N)]
pillars.sort()
highestPillar = max(pillars, key= lambda x: x[1])[1]
result = 0
currentPillar = pillars[0]
for i in range(1, N):
    if currentPillar[1] == highestPillar:
        break
    if pillars[i][1] > currentPillar[1]:
        result += (pillars[i][0] - currentPillar[0]) * (highestPillar - currentPillar[1])
        currentPillar = pillars[i]

currentPillar = pillars[-1]
for i in range(N-2, -1, -1):
    if currentPillar == highestPillar:
        break
    if pillars[i][1] > currentPillar[1]:
        result += abs(pillars[i][0] - currentPillar[0]) * abs(currentPillar[1] - highestPillar)
        currentPillar = pillars[i]
result = highestPillar * (pillars[-1][0]+1- pillars[0][0]) - result
print(result)
