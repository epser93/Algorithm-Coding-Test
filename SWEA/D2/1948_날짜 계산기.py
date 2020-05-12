T = int(input())
for t in range(T):
    month = list(map(int,input().split()))
    day = [31,28,31,30,31,30,31,31,30,31,30,31]
    result = 0
    if month[0] == month[2]:
        result = month[3] - month[1] + 1
    else:
        for i in range(month[0]+1,month[2]):
            result += day[i-1]
        result = result + day[month[0]-1]-month[1] + month[3] + 1
    print('#{} {}'.format(t+1,result))