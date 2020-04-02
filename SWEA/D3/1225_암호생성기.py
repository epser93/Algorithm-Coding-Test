while 1:
    try:
        n = int(input())
        arr = list(map(int,input().split()))
        break_point = 0
        while 1:
            for i in range(1,6):
                change = arr.pop(0) - i
                if change <= 0:
                    change = 0
                    arr.append(change)
                    break_point = 1
                    break
                arr.append(change)
            if break_point == 1:
                break
        print(f'#{n}',*arr)

    except EOFError:
        break