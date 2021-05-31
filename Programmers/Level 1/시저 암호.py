def solution(s, n):
    result = ""
    for string in s:
        if string == " ":
            result += " "
            continue
        if 65 <= ord(string) <= 90:
            if ord(string) + n > 90:
                result += chr(ord(string) + n - 26)
            else:
                result += chr(ord(string) + n)
        elif 97 <= ord(string) <= 122:
            if ord(string) + n > 122:
                result += chr(ord(string) + n - 26)
            else:
                result += chr(ord(string) + n)
    return result

if __name__ == "__main__":
    print(solution("AB", 1))
    print(solution("z", 1))
    print(solution("a B z", 4))