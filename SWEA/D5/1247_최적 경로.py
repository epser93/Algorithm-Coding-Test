def dfs(idx, before, distance):
    global min_distance
    if min_distance < distance:
        return
    if idx == N:
        distance += abs(location[before]-location[2])+abs(location[before+1]-location[3])
        if distance < min_distance:
            min_distance = distance 
        return
    for i in range(4,(N+2)*2,2):
        if not visit[i]:
            visit[i] = 1
            new_distance = distance + abs(location[before]-location[i])+abs(location[before+1]-location[i+1])
            dfs(idx+1,i,new_distance)
            visit[i] = 0

for t in range(1,int(input())+1):
    N = int(input())
    location = list(map(int,input().split()))
    visit = [0]*((N+2)*2)
    min_distance = 99999999999999
    dfs(0,0,0)
    print('#{} {}'.format(t,min_distance))
