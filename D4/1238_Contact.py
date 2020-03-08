def bfs(start_node):
    next_queue = [start_node]
    while 1:
        queue = next_queue[:]
        temp_queue = queue[:]
        next_queue = []
        while queue:
            q = queue.pop(0)
            if q in contact:
                for node in contact[q]:
                    if not visit[node]:
                        visit[node] = 1
                        next_queue.append(node)
        if len(next_queue) == 0:
            return max(temp_queue)
            
for t in range(10):
    data, start = map(int,input().split())
    number = list(map(int,input().split()))
    visit = [0] * (max(number)+1)
    contact ={}
    for i in range(0,len(number),2):
        if number[i] not in contact:
            contact[number[i]] = [number[i+1]]
        else:
            if number[i+1] not in contact[number[i]]:
                contact[number[i]].append(number[i+1])
    visit[start] = 1
    print('#{} {}'.format(t+1,bfs(start)))