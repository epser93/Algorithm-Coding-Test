from collections import deque

def bfs(start,end):
    queue = deque()
    queue.append([start,0])
    visit = [0]*1000001
    while queue:
        q = queue.popleft()
        if visit[q[0]]:
            continue
        visit[q[0]] = 1
        for i in range(4):
            if i == 0:
                new_result = q[0] + 1
            elif i == 1:
                new_result = q[0] - 1
            elif i == 2:
                new_result = q[0] * 2
            elif i == 3:
                new_result = q[0] - 10

            if new_result == end:
                return q[1]+1
            elif new_result <= 1000000 and new_result > 0:
                queue.append([new_result,q[1]+1])

for t in range(1,int(input())+1):
    N, M = map(int,input().split())
    print('#{} {}'.format(t,bfs(N,M)))
