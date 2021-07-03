import sys
input = sys.stdin.readline

def dfs(idx, person):
    if idx == 2:
        return
    for friend in relations[person]:
        if not visit[friend] and relations[friend]:
            visit[friend] = 1
            inviteSet.add(friend)
            dfs(idx+1, friend)
            visit[friend] = 0

n = int(input())
m = int(input())
relations = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)
visit = [0] * (m + 1)
inviteSet = set()
if relations[1]:
    visit[1] = 1
    dfs(0, 1)
    print(len(inviteSet))
else:   
    print(0)


