def johab(idx,end,result):
    global max_result
    if idx == end:
        if result > max_result:
            max_result = result
        return
    if result <= max_result:
        return 
    for i in range(N):
        if not visit[i]:
            new_result = result * probability[idx][i] * 0.01
            visit[i] = 1
            johab(idx+1,end,new_result)
            visit[i] = 0
        
T = int(input())
for t in range(T):
    N = int(input())
    probability = []
    for _ in range(N):
        probability.append(list(map(int,input().split())))
    visit =[0 for _ in range(N)]
    max_result = -99999999
    johab(0,N,1)
    print("#{} {}".format(t+1,format(max_result*100,".6f")))