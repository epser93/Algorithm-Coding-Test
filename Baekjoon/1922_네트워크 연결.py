import sys

def find_parent(parent, target):
    if parent[target] != target:
        parent[target] = find_parent(parent, parent[target])
    return parent[target]

def union(parent, root1, root2):
    if root1 < root2:
        parent[root2] = root1
    else:
        parent[root1] = root2

input = sys.stdin.readline
N = int(input())
M = int(input())
parent = [x for x in range(N+1)]
graph = []
result = 0
for _ in range(M):
    graph.append(list(map(int, input().split())))
graph.sort(key=lambda x : x[-1])
for a, b, c in graph:
    a_parent = find_parent(parent, a)
    b_parent = find_parent(parent, b)
    if a_parent != b_parent:
        union(parent, a_parent, b_parent)
        result += c
print(result)