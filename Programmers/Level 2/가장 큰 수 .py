def solution(numbers):
    return str(int(''.join(sorted(list(map(str, numbers)), key=lambda x : x * 4, reverse=True))))

if __name__ == "__main__":
    print(solution([6, 10, 2]))
    print(solution([3, 30, 34, 5, 9]))
    print(solution([0,0,0,0]))  