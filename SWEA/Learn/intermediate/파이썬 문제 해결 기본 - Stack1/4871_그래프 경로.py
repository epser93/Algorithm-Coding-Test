def DFS(node,end_node):
    if visit[end_node] == 1:
        return 1
    for i in way[node]:
        if visit[i] == 0:
            visit[i] = 1
            result = DFS(i,end_node)
            visit[i] = 0
            if result == 1:
                return 1
    return 0
T = int(input())
for t in range(T):
    V, E = map(int,input().split())
    arr = []
    way = [[] for _ in range(V+1)]
    for _ in range(E):
        arr.append(list(map(int,input().split())))
    for i in range(E):
        a = arr[i][0]
        b = arr[i][1]
        way[a].append(b)
    S, G = map(int,input().split())
    visit = [0 for _ in range(V+1)]
    print('#{} {}'.format(t+1,DFS(S,G)))