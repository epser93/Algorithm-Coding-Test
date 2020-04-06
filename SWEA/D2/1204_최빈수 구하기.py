T = int(input())
for t in range(T):
    n = int(input())
    arr = list(map(int,input().split()))
    score = {}
    for point in arr:
        if point not in score:
            score[point] = 1
        else:
            score[point] += 1
    max_ = 0
    result = 0
    for key,value in score.items():
        if value > max_:
            max_ = value
            result = key
    print('#{} {}'.format(t+1,result))
    