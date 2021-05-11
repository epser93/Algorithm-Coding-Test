def solution(lottos, win_nums):
    correct = 0
    zeroCnt = 0
    for lotto in lottos:
        if lotto != 0:
            if lotto in win_nums:
                correct += 1
        else:
            zeroCnt += 1
    if correct == 0:
        lowestRank = 6
    else:
        lowestRank = 7 - correct
    
    correct += zeroCnt

    if correct == 0:
        highestRank = 6
    else:
        highestRank = 7 - correct

    answer = [highestRank, lowestRank]
    return answer


if __name__=="__main__":
    print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
    print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
    print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))
