for t in range(1,int(input())+1):
    container, truck = map(int,input().split())
    weight = sorted(list(map(int,input().split())),reverse=True)
    truck_power = sorted(list(map(int,input().split())),reverse=True)
    arr = []
    for truck_num in truck_power:
        for i in range(len(weight)):
            if truck_num >= weight[i]:
                arr.append(weight[i])
                weight.pop(i)
                break
    print('#{} {}'.format(t,sum(arr)))
