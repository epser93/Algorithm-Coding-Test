T = int(input())
for w in range(T):
    n = int(input())
    color = []
    arr = [[0 for i in range(10)] for j in range(10)]
    for s in range(n):
        color.append(list(map(int, input().split())))
    for color1 in color:
        for k in range(color1[0],color1[2]+1):
            for l in range(color1[1],color1[3]+1):
                arr[k][l] += color1[4]
    sum = 0
    for cnt in range(len(arr)):
        sum += arr[cnt].count(3)
    print('#{} {}'.format(w+1, sum))