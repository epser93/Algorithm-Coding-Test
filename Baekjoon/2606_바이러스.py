def dfs(start):
    global cnt, connections, visit
    if connections.get(start):
        for dest in connections[start]:
            if not visit[dest- 1]:
                cnt += 1
                visit[dest - 1] = 1
                dfs(dest)
    return 

M = int(input())
N = int(input())
connections = {}
visit = [0] * M
visit[0] = 1
cnt = 0
for _ in range(N):
    start, end = map(int,input().split())
    if not connections.get(start):
        connections[start] = [end]
    else:
        connections[start].append(end)
    if not connections.get(end):
        connections[end] = [start]
    else:
        connections[end].append(start)
dfs(1)
print(cnt)
