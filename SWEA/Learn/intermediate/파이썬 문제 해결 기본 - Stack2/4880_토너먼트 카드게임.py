def card(start,end):
    if start == end:
        return start
    num1 = card(start,(start+end)//2)
    num2 = card((start+end)//2+1,end)
    return win(num1,num2)

def win(x,y):
    if (arr[x-1] == 1 and arr[y-1] == 3) or (arr[x-1] == 1 and arr[y-1] == 1):
        return x
    elif (arr[x-1] == 2 and arr[y-1] == 1) or (arr[x-1] == 2 and arr[y-1] == 2):
        return x
    elif (arr[x-1] == 3 and arr[y-1] == 2) or (arr[x-1] == 3 and arr[y-1] == 3):
        return x
    return y
T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    start = 1
    end = len(arr)
    print('#{} {}'.format(t+1,card(start,end)))