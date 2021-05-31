def solution(ss):
    cntP = 0
    cntY = 0
    for s in ss:
        if s.upper() == "P":
            cntP += 1
        elif s.upper() == "Y":
            cntY += 1
    return cntP == cntY

if __name__ == "__main__":
    print(solution("pPoooyY"))
    print(solution("Pyy"))