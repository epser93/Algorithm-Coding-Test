def solution(s):
    result = []
    s = s.split(" ")
    for word in s:
        temp = ''
        for idx, string in enumerate(word):
            if idx % 2:
                temp += string.lower()
            else:
                temp += string.upper()
        result.append(temp)
    return ' '.join(result)

if __name__ == "__main__":
    print(solution("try hello world"))