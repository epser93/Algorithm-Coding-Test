import sys

input = sys.stdin.readline

A, N = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answers = []
lengthOfArr = len(arr)
answer = 0
for i in range(lengthOfArr):
    answer += arr[i]
    answers.append(answer)

results = []
questions = []
for _ in range(N):
    questions.append(list(map(int, input().split())))

for question in questions:
    L = question[0] - 1
    R = question[1] - 1
    if L == 0:
        results.append(answers[R])
    else:
        results.append(answers[R] - answers[L - 1])

for result in results:
    print(result)