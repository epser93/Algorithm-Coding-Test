import sys

input = sys.stdin.readline

N, K = map(int, input().split())
directions = {}
visit = [1] + [0] * N
cnt = 0
position = 0
for i in range(N):
    directions[i] = int(input())

while 1:
    if position == K:
        break
    position = directions[position]
    if visit[position]:
        cnt = -1
        break
    cnt += 1
    visit[position] = 1
print(cnt)