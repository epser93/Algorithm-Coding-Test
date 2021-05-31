def solution(n):
    result = 0
    for num in str(n):
        result += int(num)
    return result

if __name__ == "__main__":
    print(solution(123))
    print(solution(987))