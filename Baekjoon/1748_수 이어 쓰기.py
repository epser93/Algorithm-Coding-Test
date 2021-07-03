N = int(input())
numSize = len(str(N))
result = 0
while numSize != 0:
    if 10 ** (numSize-1) <= N < 10 ** numSize:
        num = (N - (10 ** (numSize-1))) * numSize
        N  -= (N - (10 ** (numSize-1)))
    elif N == 10 ** numSize:
        num = (10 ** numSize - 10 ** (numSize - 1)) * numSize
        N -= (10 ** numSize - 10 ** (numSize - 1))
    result += (num + 1)
    numSize -= 1
print(result)