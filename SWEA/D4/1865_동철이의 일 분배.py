def johab(idx,end,result):
    global max_result
    if idx == end:
        if result > max_result:
            max_result = result
        return
    if result <= max_result: # 가지치기 중간까지의 결과값이 max보다 작으면 앞으로도 가능성 없음 // 곱하는 값들이 1보다 작기떄문에
        return 
    for i in range(N):
        if not visit[i]: # 방문 하지 않았다면 == 일이 선택되지 않았다면
            new_result = result * probability[idx][i] * 0.01 
            visit[i] = 1 
            johab(idx+1,end,new_result)
            visit[i] = 0 # return 되면서 방문 배열 초기화
        
T = int(input())
for t in range(T):
    N = int(input())
    probability = []
    for _ in range(N):
        probability.append(list(map(int,input().split())))
    visit =[0 for _ in range(N)] # 방문 배열 == 일
    max_result = -99999999
    johab(0,N,1)
    print("#{} {}".format(t+1,format(max_result*100,".6f")))