import sys, heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])
start, end = map(int, input().split())
distances = [float('inf') for _ in range(N+1)]
distances[start] = 0
queue = []
heapq.heappush(queue, [distances[start], start]) # (거리, 노드시작점)
while queue:
    current_distance, current_node = heapq.heappop(queue)
    if distances[current_node] < current_distance:
        continue
    for destination, distance in graph[current_node]:
        new_distance = distance + current_distance
        if new_distance < distances[destination]:
            distances[destination] = new_distance
            heapq.heappush(queue, [new_distance, destination])
print(distances[end])