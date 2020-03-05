T = int(input())
for t in range(T):
    N = int(input())
    score = list(map(int,input().split()))
    score_visit = [1] + [0] * sum(score)
    score2 = [0]
    for point in score:
        for i in range(len(score2)):
            if not score_visit[point+score2[i]]:
                score_visit[point+score2[i]] = 1
                score2.append(point+score2[i])
    print('#{} {}'.format(t+1,len(score2)))