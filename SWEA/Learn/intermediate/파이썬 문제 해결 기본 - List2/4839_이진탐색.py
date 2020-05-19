def check(P,person):
    start = 1
    end = P
    cnt = 1
    c= (start + end) // 2
    while 1:
        if c == person:
            return cnt
        if c > person:
            end = c
            cnt += 1
            c= (start + end) // 2
        elif c < person:
            start = c
            cnt += 1
            c= (start + end) // 2

T= int(input())
for i in range(T):
    P,A,B = map(int,input().split())

    if check(P,A) < check(P,B):
            print("#{} {}".format(i+1,"A"))
    elif check(P,A) == check(P,B):
        print("#{} {}".format(i+1,"0"))
    else:
        print("#{} {}".format(i+1,"B"))
