def delete(s):
    result = []
    prev = ""
    for string in s:
        if string == prev:
            result.pop()
            if result[-1:] != []:
                prev = result[-1]
            else:
                prev = ""
        else:
            result.append(string)
            prev = string
    return result

def solution(s):
    if len(s) % 2:
        return 0
    if delete(s):
        return 0
    return 1

if __name__ == "__main__":
    print(solution("baabaa"))
    print(solution("cdcd"))