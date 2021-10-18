from collections import deque

def findIndex(arrays, target):
    for idx, array in enumerate(arrays):
        if array[0] == target:
            return idx
    return -1

N = int(input())
M = int(input())
recommands = list(map(int, input().split()))
result = []
queue = []
students = {x+1 : 0 for x in range(100)}
for day, recommand in enumerate(recommands):
    if len(queue) != N and not students[recommand]:
        queue.append([recommand, 1, day]) # 학생번호, 추천수, 추가일자
        students[recommand] = 1
        continue
    if not students[recommand]:
        queue.sort(key=lambda x: (x[1], x[2]))
        delete_target_student = queue.pop(0)[0]
        students[delete_target_student] = 0
        students[recommand] = 1
        queue.append([recommand, 1, day])
    else:
        student_idx = findIndex(queue, recommand)
        queue[student_idx][1] += 1
for student in sorted(queue):
    result.append(student[0])
print(*result)