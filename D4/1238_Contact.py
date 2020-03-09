def bfs(start_node): # BFS 탐색 단계별로 진행함으로서 마지막 연락을 알 수 있음
    next_queue = [start_node]
    while 1:
        queue = next_queue[:] # 단계별로 진행시키기 위해 복사 큐를 만듬
        temp_queue = queue[:]
        next_queue = []
        while queue:
            q = queue.pop(0)
            if q in contact:
                for node in contact[q]:
                    if not visit[node]:
                        visit[node] = 1
                        next_queue.append(node) # 다음 단계 큐에 append
        if len(next_queue) == 0:
            return max(temp_queue)
            
for t in range(10):
    data, start = map(int,input().split())
    number = list(map(int,input().split()))
    visit = [0] * (max(number)+1)
    contact ={}
    for i in range(0,len(number),2): # 경로 딕셔너리로 저장
        if number[i] not in contact:
            contact[number[i]] = [number[i+1]]
        else:
            if number[i+1] not in contact[number[i]]: # 중복 방지
                contact[number[i]].append(number[i+1])
    visit[start] = 1
    print('#{} {}'.format(t+1,bfs(start)))