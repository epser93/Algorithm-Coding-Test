def dfs(start_node,visits):
    visits.append(start_node)
    if len(visits) == N:
        return visits
    for i in range(1,len(matrix[start_node])):
        if matrix[start_node][i] and i not in visits:
            visits = dfs(i,visits)
    return visits

def bfs(start_node):
    queue = [start_node]
    visit = [start_node]
    while 1:
        if len(queue) == 0:
            return visit
        pop = queue.pop(0)
        for i in range(1,len(matrix[pop])):
            if matrix[pop][i] and i not in visit:
                visit.append(i)
                queue.append(i)
        


N, M, V = map(int,input().split())
matrix = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    arr = list(map(int,input().split()))
    matrix[arr[0]][arr[1]] = 1
    matrix[arr[1]][arr[0]] = 1

print(*dfs(V,[]))
print(*bfs(V))