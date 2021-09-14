import sys
input = sys.stdin.readline

def find_parent(parent, target):
    if parent[target] != target:
        parent[target] = find_parent(parent, parent[target])
    return parent[target]

def union(parent, root1, root2):
    if root1 < root2:
        parent[root2] = root1
    else:
        parent[root1] = root2

N, M = map(int, input().split())
parent = [x for x in range(N+1)]
result = 0
graph = []
max_cost = float('-inf')
for _ in range(M):
    graph.append(list(map(int, input().split())))
graph.sort(key=lambda x: x[-1])
for start, end, cost in graph:
    a_parent = find_parent(parent, start)
    b_parent = find_parent(parent, end)
    if a_parent != b_parent:
        union(parent, a_parent, b_parent)
        result += cost
        if cost > max_cost:
            max_cost = cost
print(result - max_cost)