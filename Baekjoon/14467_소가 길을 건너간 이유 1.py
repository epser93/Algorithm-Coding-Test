N = int(input())
cowPosition = {}
cnt = 0
for _ in range(N):
    cow, position = map(int, input().split())
    if cow not in cowPosition.keys():
        cowPosition[cow] = position
    elif cowPosition.get(cow) != position:
        cowPosition[cow] = position
        cnt += 1
print(cnt)