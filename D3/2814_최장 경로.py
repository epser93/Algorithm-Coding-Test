def dfs(start,cnt):
    global max_cnt
    for i in way[start]: # start 노드가 시작인 딕셔너리 값이 존재한다면
        if not visit[i-1]: # 방문도 안했으면
            visit[i-1] = 1 # 방문 체크해주고
            dfs(i,cnt+1) # 그 값이 다시 start 노드가 되도록 dfs
            visit[i-1] = 0 # 백트래킹 후 방문 해제
    if cnt > max_cnt: # 탐색 다하고 max값 비교
        max_cnt = cnt

for t in range(1,int(input())+1):
    N, M = map(int,input().split())
    way = {}
    visit = [0 for _ in range(N)]
    max_cnt = 1
    # 노드경로 딕셔너리 만들기 / 무방향 == 양방향
    for i in range(M):
        a, b = map(int,input().split())
        if a not in way:
            way[a] = [b]
        else:
            if b not in way[a]:
                way[a].append(b)

        if b not in way:
            way[b] = [a]
        else:
            if a not in way[b]:
                way[b].append(a)
    
    # key == 시작노드
    for key,value in way.items():
        dfs(key,0)

    print('#{} {}'.format(t,max_cnt))