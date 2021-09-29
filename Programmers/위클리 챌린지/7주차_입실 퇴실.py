def solution(enter, leave):
    answer = [0] * len(enter)
    visit = [[0 for _ in range(1001)] for _ in range(1001)]
    enters = enter
    for number in leave:
        index = enters.index(number)
        if index != 0:
            for i in range(index):
                for j in range(i+1, index+1):
                    if not visit[enters[i]][enters[j]]:
                        answer[enters[i]-1] += 1
                        answer[enters[j]-1] += 1
                        visit[enters[i]][enters[j]] = 1
        enters.pop(index)
    return answer