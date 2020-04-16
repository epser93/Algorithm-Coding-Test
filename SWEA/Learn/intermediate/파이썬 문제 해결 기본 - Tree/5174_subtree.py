def dfs(start_node):
    global cnt
    if len(node[start_node]) == 1:
        return
    for i in range(1,len(node[start_node])):
        cnt += 1
        dfs(node[start_node][i])


for t in range(1,int(input())+1):
    E, N = map(int,input().split())
    node = [[0] for _ in range(E+2)]
    temp = list(map(int,input().split()))
    cnt = 1
    for idx in range(0,len(temp),2):
        node[temp[idx]].append(temp[idx+1])
    dfs(N)
    print('#{} {}'.format(t,cnt))