def solution(n, lost, reserve):
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    answer = n - len(new_lost)
    for lost_member in new_lost:
        if lost_member-1 in new_reserve:
            answer += 1
            new_reserve.remove(lost_member-1)
        elif lost_member+1 in new_reserve:
            answer += 1
            new_reserve.remove(lost_member+1)
    return answer