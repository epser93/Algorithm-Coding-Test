T = int(input()) 
for t in range(T):
    N = int(input())  
    dic = {}

    for i in range(1,5001): # 딕셔너리 1~5000까지 0으로 초기화 
        dic[i] = 0

    for i in range(N): # 딕셔너리에 way 범위에 해당되는 value값 1씩 늘리기
        start, end = map(int,input().split())
        for j in range(start,end+1):
            dic[j] += 1

    P = int(input())
    result = []   

    for i in range(P): # result 리스트에 해당 정류장에 맞는 value값 저장
        result.append(dic[int(input())])

    print(f'#{t+1}', *result)