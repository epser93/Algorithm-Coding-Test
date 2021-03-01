import sys

input = sys.stdin.readline
N , X = map(int, input().split())

if 26 * N < X or N > X:
    result = '!'
else:
    result = ['A'] * N
    X -= N
    idx = N - 1
    while X > 0:
        if X >= 25:
            result[idx] = 'Z'
            idx -= 1
            X -= 25
        else:
            result[idx] = chr(65 + X)
            break
print(''.join(result))

# 2 52 ZZ
# 3 51 AWZ
# 2 26 AY
# 2 27 AZ
# 2 25 AW