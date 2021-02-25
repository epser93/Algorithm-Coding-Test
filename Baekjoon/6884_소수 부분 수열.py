import sys

def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5 + 1)):
        if number % i == 0:
            return False
    return True

for _ in range(int(sys.stdin.readline())):
    numList = list(map(int, sys.stdin.readline().split()))
    lengthOfNumList = numList[0]
    flag = False
    for i in range(2, lengthOfNumList + 1):
        for j in range(lengthOfNumList - i + 1):
            if j == 0:
                sumOfNum = sum(numList[1 : 1 + i])
            elif i == lengthOfNumList:
                sumOfNum += numList[1] 
            else:
                sumOfNum += (numList[i + j] - numList[j])
            if isPrime(sumOfNum):
                print("Shortest primed subsequence is length {}: {}".format(i, ' '.join(map(str, numList[1 + j : j + i + 1]))))
                flag = True
                break
        if flag:
            break
    else:
        print("This sequence is anti-primed.")