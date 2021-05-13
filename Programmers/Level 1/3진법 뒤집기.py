def tenToThree(n):
    result = 0
    for i in range(len(n) - 1, -1, -1):
        result += (3 ** (len(n) - 1 - i)) * int(n[i])
    return result

def reverseThreeToTen(n):
    result = ""
    while n:
        result += str(n % 3)
        n //= 3
    return result

def solution(n):
    threeDigitNum = reverseThreeToTen(n)
    result = tenToThree(threeDigitNum)
    return result

if __name__ == "__main__":
    print(solution(45))
    print(solution(125))
    