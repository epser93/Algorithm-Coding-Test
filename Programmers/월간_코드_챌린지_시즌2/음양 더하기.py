def solution(absolutes, signs):
    answer = 0
    n = len(absolutes)
    for i in range(n):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer += absolutes[i] * (-1)
    return answer

if __name__ == "__main__":
    print(solution([4,7,12], [True,False,True]))
    print(solution([1,2,3], [False,False,True]))