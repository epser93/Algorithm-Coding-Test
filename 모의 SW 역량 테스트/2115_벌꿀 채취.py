def profit(array1, array2): # 이득계산
    global max_honey
    global answer
    answer = []
    bubun(0,array1,0,0)
    max1 = max(answer)
    answer = []
    bubun(0,array2,0,0)
    max2 = max(answer)
    if max1 + max2 > max_honey:
        max_honey = max1+max2
    return 

def number2(row,col):
    arr2 = []
    if col+2*M-1 < N: # 2번 벌꿀통이 1번과 같은 행에 존재하는지 확인
        for i in range(M):
            arr2.append(honey[row][col+M+i]) # 2번 사람 벌꿀통

    profit(arr1,arr2) # 같은 행에 존재하면 이득 계산
    
    for rows in range(row+1,N): #그 다음행부터 M칸 만큼씩 전부 타맥
        for col in range(N):
            if col+M-1 < N:
                arr2 = []
                for i in range(M):
                    arr2.append(honey[rows][col+i])
                    profit(arr1,arr2)

def bubun(idx,a,summ,result): # 부분집합 만드는 부분
    if summ > C: # 가지치기
        return
    if idx == len(a) and summ <= C:
        answer.append(result)
        return 
    bubun(idx+1,a,summ+a[idx],result+a[idx]**2)
    bubun(idx+1,a,summ,result)

T = int(input())
for t in range(T):
    N, M, C = map(int,input().split()) # N = 맵크기 / M = 벌통 개수 / C  = 꿀 최대양
    honey = [list(map(int,input().split())) for _ in range(N)]
    max_honey = -9999999
    for x in range(N-1):
        for y in range(N): # 열을 한칸 씩 민다
            if y+M-1 < N: # 현재 열에서 M만큼 더한 위치가 맵 범위 안이면 벌꿀 채취가능
                arr1 = []
                for i in range(M): 
                    arr1.append(honey[x][y+i]) # 1번 사람 벌꿀통
                    number2(x,y) # 2번 사람 벌꿀통 찾으러들어감
    print('#{} {}'.format(t+1,max_honey))