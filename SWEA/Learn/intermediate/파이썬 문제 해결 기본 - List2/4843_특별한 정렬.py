T = int(input())
for j in range(T):
    n = int(input())
    arr = list(map(int,input().split()))
    print("#{}".format(j+1), end=" ")
    for i in range(1,11):
        if i % 2 == 1:
            print(arr.pop(arr.index(max(arr))), end=" ")
        else:
            print(arr.pop(arr.index(min(arr))), end=" ")
    print()