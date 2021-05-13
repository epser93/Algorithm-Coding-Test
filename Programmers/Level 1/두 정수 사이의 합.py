def solution(a, b):
    result = 0
    if a > b:
        start, end = b, a
    else:
        start, end = a, b
    for num in range(start, end + 1):
        result += num
    return result

if __name__ == "__main__":
    print(solution(3, 5))
    print(solution(3, 3))
    print(solution(5, 3))
    