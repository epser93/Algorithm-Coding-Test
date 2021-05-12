def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s = sorted(s, key=lambda x : len(x))
    for idx, z in enumerate(s):
        if idx == 0:
            answer.append(int(z))
            present = {z}
        else:
            z = set(z.split(","))
            for num in (z - present):
                answer.append(int(num))
            present = z
    return answer

if __name__ == "__main__":
    print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
    print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
    print(solution("{{20,111},{111}}"))
    print(solution("{{123}}"))
    print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
