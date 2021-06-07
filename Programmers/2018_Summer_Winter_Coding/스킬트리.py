from collections import deque

def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        skillOrder = deque(skill)
        for oneSkill in skill_tree:
            if oneSkill in skill:
                if skillOrder[0] != oneSkill:
                    break
                skillOrder.popleft()
        else:
            answer += 1
    return answer

if __name__ == "__main__":
    print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))