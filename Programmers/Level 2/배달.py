from collections import deque

def solution(N, roads, K):
    mapp = {}
    result = 0
    costMap = [float('inf') for _ in range(N + 1)]
    costMap[1] = 0
    nextNode = deque([1])

    for start, end, cost in roads:
        if mapp.get(start) == None:
            mapp[start] = [(end, cost)]
        else:
            mapp[start].append((end, cost))
        if mapp.get(end) == None:
            mapp[end] =[(start,cost)]
        else:
            mapp[end].append((start, cost))
    
    while nextNode:
        node = nextNode.popleft()
        for dest, cost in mapp[node]:
            if costMap[node] + cost > costMap[dest]:
                continue
            costMap[dest] = costMap[node] + cost
            nextNode.append(dest)

    for cost in costMap:
        if cost <= K:
            result += 1

    return result

if __name__ == "__main__":
    print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
    print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))
    