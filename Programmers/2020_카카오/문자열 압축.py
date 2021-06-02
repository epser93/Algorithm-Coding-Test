def compress(s, num):
    result = []
    cnt = 1
    for i in range(0, len(s) + 1, num):
        if not result:
            result.append(s[i:i+num])
            continue
        if result[-1] == s[i:i+num]:
            cnt += 1
        else:
            if cnt > 1:
                result[-1] = str(cnt) + result[-1]
            cnt = 1
            result.append(s[i:i+num]) 
    return len(''.join(result))
        

def solution(s):
    minLen = float('inf')
    for i in range(1, len(s) + 1):
        compressLen = compress(s, i)
        if compressLen < minLen:
            minLen = compressLen
    return minLen

if __name__ == "__main__":
    print(solution("aabbaccc"))
    print(solution("ababcdcdababcdcd"))
    print(solution("abcabcdede"))
    print(solution("abcabcabcabcdededededede"))
    print(solution("xababcdcdababcdcd"))