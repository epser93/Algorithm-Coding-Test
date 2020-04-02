for t in range(int(input())):
    N, M = map(int,input().split())
    pizza = list(map(int,input().split()))
    queue = []
    q2 = []
    for idx,piz in enumerate(pizza):
        queue.append([idx+1,piz])

    for _ in range(N):
        q2.append(queue.pop(0))

    while 1:
        if len(q2) == 1:
            print('#{} {}'.format(t+1,q2[0][0]))
            break
        else:
            cheese = q2.pop(0)
            cheese[1] //= 2
            if cheese[1]:
                q2.append(cheese)
            else:
                if queue:
                    q2.append(queue.pop(0))