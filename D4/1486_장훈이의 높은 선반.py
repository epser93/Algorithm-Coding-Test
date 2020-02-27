def perm(idx,summ):
    global result
    if summ > result: # 가지 치기 
        return
    if idx >= N: # 부분집합이 완성 되었을 때 기존 result와 비교
        if B <= summ <= result:
            result = summ
        return
    for i in range(2): # 리스트 요소를 더할 경우 / 더 하지 않을 경우로 분기를 나눔
        perm(idx+1,summ+case[idx]*i)

T = int(input())
for t in range(T):
    N ,B = map(int,input().split())
    case = list(map(int,input().split()))
    summ = 0
    result = 99999999
    perm(0,0)
    print(f'#{t+1} {result-B}')