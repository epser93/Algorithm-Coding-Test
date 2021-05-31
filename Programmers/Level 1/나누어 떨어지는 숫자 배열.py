def solution(arr, divisor):
    result = []
    for num in arr:
        if num % divisor == 0:
            result.append(num)
    if result[-1:] == []:
        result.append(-1)
    return sorted(result)

if __name__ == "__main__":
    print(solution([5, 9, 7, 10], 5))
    print(solution([2, 36, 1, 3], 1))
    print(solution([3,2,6], 10))