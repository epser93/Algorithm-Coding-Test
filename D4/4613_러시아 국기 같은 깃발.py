T = int(input())
for t in range(T):
    N, W = map(int,input().split())
    mapp = [input() for _ in range(N)]
    min_cnt = 99999999
    for i in range(1,N-1): # W줄 개수 
        for j in range(1,N-1): # B줄 개수
            if i+j >= N: # W + B 줄이 전체 행 길이 이상이면 R줄 못쓰니까 break
                break
            for k in range(1,N-1): # R줄 개수
                if i+j+k == N: # W+B+R줄 합 == 전체 행개수이라면
                    cnt = 0
                    result = 0
                    for a in range(0,i): # 각 행 별 W,R,B 개수 파악
                        cnt += mapp[a].count('W')
                    for b in range(i,i+j):
                        cnt += mapp[b].count('B')
                    for c in range(i+j,i+j+k):
                        cnt += mapp[c].count("R")
                    result = W*N - cnt # 전체 셀 개수에서 각 행 별 W,R,B 개수를 빼면 수정해야할 개수가 나옴
                    if result < min_cnt:
                        min_cnt = result
    print('#{} {}'.format(t+1,min_cnt))
