def solution(n):
    result = 0
    for num in range(1, n + 1):
        if n % num == 0:
            result += num
    return result

if __name__ == "__main__":
    print(solution(12))
    print(solution(5))