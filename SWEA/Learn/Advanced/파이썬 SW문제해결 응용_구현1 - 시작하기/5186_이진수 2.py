for t in range(1, int(input())+1):
    num = float(input())
    result = ''
    cnt = 0
    while 1:
        new_num = num * 2
        cnt += 1
        if cnt >= 13:
            result = 'overflow'
            break
        if new_num == 1:
            mok = '1'
            result += mok
            break
        elif new_num > 1:
            mok = '1'
            num = new_num - 1
        else:
            mok = '0'
            num = new_num 
        result += mok
    print('#{} {}'.format(t,result))