import sys
sys.setrecursionlimit(10000) 

def dfs(start):
    visit[start] = 1
    for way in ways[start]:
        if not visit[way]:
            dfs(way)

N, M = map(int, input().split())
ways = [[] for _ in range(N+1)]
visit = [0] * (N + 1)
cnt = 0
for _ in range(M):
    a, b = map(int, input().split())
    ways[a].append(b)
    ways[b].append(a)

for i in range(1, N+1):
    if not visit[i]:
        dfs(i)
        cnt += 1
print(cnt)
