def solution(s):
    return ' '.join([str(min(map(int,s.split()))), str(max(map(int,s.split())))])

if __name__ == "__main__":
    print(solution("1 2 3 4"))
    print(solution("-1 -2 -3 -4"))
    print(solution("-1 -1"))