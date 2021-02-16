# https://www.acmicpc.net/problem/1535

def getMaxjoy(prev, health, joy):
    global maxJoy
    if health <= 0:
        return
    if joy > maxJoy:
        maxJoy = joy
    for i in range(prev + 1, len(healthList)):
        getMaxjoy(i, health - healthList[i], joy + joyList[i])

N = int(input())
healthList = list(map(int, input().split()))
joyList = list(map(int, input().split()))
visit = [0 for _ in range(N)]
maxJoy = float("-inf")

getMaxjoy(-1, 100, 0)

print(maxJoy)