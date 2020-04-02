T = int(input())
for t in range(T):
    word = input()
    H = int(input())
    loc = list(map(int,input().split()))
    cnt = [0] * (len(word)+1) # 자리 카운팅 // 한번에 붙일예정
    for i in loc: # 자리 카운팅
        cnt[i] += 1
    answer = [] # 결과값 들어갈 배열
    for idx,j in enumerate(cnt):# idx = 0 이면 하이픈만
        if idx > 0: # idx > 0이면 word값 배열에 넣고 카운팅 수만큼 하이픈 
            answer.append(word[idx-1]) 
        for _ in range(cnt[idx]):
            answer.append('-')
    print('#{} {}'.format(t+1,''.join(answer)))