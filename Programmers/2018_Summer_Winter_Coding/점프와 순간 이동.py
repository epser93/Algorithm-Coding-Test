def solution(n):
    return bin(n).count('1')

if __name__ == "__main__":
    print(solution(5))
    print(solution(6))
    print(solution(5000))