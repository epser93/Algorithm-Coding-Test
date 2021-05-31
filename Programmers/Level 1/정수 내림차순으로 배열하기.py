def solution(n):
    arr = sorted(list(str(n)), reverse=True)
    return int(''.join(arr))

if __name__ == "__main__":
    print(solution(118372))