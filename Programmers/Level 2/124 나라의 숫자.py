def solution(n):
    threeDigit = ['4', '1', '2']
    num = ''
    while n != 0:
        num = threeDigit[n % 3] + num
        if n % 3 == 0:
            n = (n - 1) // 3
        else:
            n //= 3
    return num

if __name__ == "__main__":
    print(solution(1))
    print(solution(2))
    print(solution(3))
    print(solution(4))
    print(solution(9))
    print(solution(10))
