dic = {
    '0': 0, 
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    'A' : 10,
    'B' : 11,
    'C' : 12,
    'D' : 13,
    'E' : 14,
    'F' : 15
}

for t in range(1, int(input())+1):
    n, number = map(str,input().split())
    new_result = ''
    for a in number:
        result = ''
        num = dic[a]
        for i in range(4):
            ans = num % 2
            num //= 2
            result = str(ans) + result
        new_result += result

    print('#{} {}'.format(t,new_result))