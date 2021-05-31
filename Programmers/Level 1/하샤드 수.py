def solution(x):
    sumNum = 0
    for num in str(x):
        sumNum += int(num)
    if not x % sumNum:
        return True
    return False

if __name__ == "__main__":
    print(solution(10))
    print(solution(12))
    print(solution(11))
    print(solution(13))