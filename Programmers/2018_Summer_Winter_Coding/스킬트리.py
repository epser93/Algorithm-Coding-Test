def getSkillSystem(skills):
    skillTree = {}
    visit = ""
    for skill in skills:
        if visit:
            skillTree[skill] = visit
        visit = skill
    return skillTree

def solution(skill, skill_trees):
    answer = 0
    skillSystem = getSkillSystem(skill)
    for skill_tree in skill_trees:
        visit = []
        isCorrect = True
        for skill in skill_tree:
            if skillSystem.get(skill) and skillSystem.get(skill) not in visit:
                isCorrect = False
                break
            visit.append(skill)
        if not isCorrect:
            continue
        answer += 1
    return answer

if __name__ == "__main__":
    print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))