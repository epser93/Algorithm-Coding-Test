def solution(answers):
    answer = []
    n1 = [1,2,3,4,5] * 2000
    n2 = [2,1,2,3,2,4,2,5] * 1250
    n3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    cnt = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == n1[i]:
            cnt[0] += 1
        if answers[i] == n2[i]:
            cnt[1] += 1
        if answers[i] == n3[i]:
            cnt[2] += 1
    for j in range(3):
        if cnt[j] == max(cnt):
            answer.append(j+1)
    return answer