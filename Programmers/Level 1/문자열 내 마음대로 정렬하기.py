def solution(strings, n):
    indicator = []
    result = []
    for idx, string in enumerate(strings):
        indicator.append([idx, string[n], string])
    indicator.sort(key=lambda x: (x[1], x[2]))
    for string in indicator:
        result.append(string[2])
    return result

if __name__ == "__main__":
    print(solution(["sun", "bed", "car"], 1))
    print(solution(["abce", "abcd", "cdx"], 2))