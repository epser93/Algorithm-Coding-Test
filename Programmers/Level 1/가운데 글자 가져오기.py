def solution(s):
    half = len(s) // 2
    if len(s) % 2:
        return s[half]
    else:
        return s[half - 1] + s[half]

if __name__ == "__main__":
    print(solution("abcde"))
    print(solution("qwer"))