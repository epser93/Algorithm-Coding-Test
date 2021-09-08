def dfs(answer):
    global arr
    aeiou = 'AEIOU'
    if len(answer) == 5:
        return
    for word in aeiou:
        arr.append(answer+word)
        dfs(answer+word)
        
def solution(word):
    global arr
    arr = []
    dfs('')
    arr.sort()
    return arr.index(word) + 1

if __name__ == "__main__":
    print(solution("AAAAE"))
    print(solution("AAAE"))
    print(solution("I"))
    print(solution("EIO"))