def bfs(start_node,end_node):
    global cnt
    cnt = 0
    queue = [start_node]
    while queue:
        for _ in range(len(queue)):
            q = queue.pop(0)
            if q == end_node:
                return
            visit[q] = 1
            for i in range(len(arr[q])):
                if not visit[arr[q][i]]:
                    queue.append(arr[q][i])
        cnt += 1
    cnt = 0
    return

for t in range(int(input())):
    V, E = map(int,input().split())
    arr = [[] for _ in range(V+1)]
    visit = [0 for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int,input().split())
        arr[a].append(b)
        arr[b].append(a)
    start, end = map(int,input().split())
    bfs(start,end)
    print('#{} {}'.format(t+1,cnt))