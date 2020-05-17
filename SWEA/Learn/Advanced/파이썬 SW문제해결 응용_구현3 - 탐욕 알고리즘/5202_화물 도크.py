for t in range(1, int(input())+1):
    N = int(input())
    timetable = [list(map(int,input().split())) for _ in range(N)]
    new_timetable = sorted(timetable, key=lambda timetable:timetable[1]-timetable[0])
    visit = []
    cnt = 0
    for start, end in new_timetable:
        if not visit:
            visit.append((start, end))
            cnt += 1
        for i in range(len(visit)):
            if (start, end) in visit:
                continue
            if visit[i][0] >= end:
                visit.insert(i,(start,end))
                cnt += 1
                break
            elif visit[-1][1] <= start:
                visit.append((start,end))
                cnt += 1
            elif visit[i][1] <= start:
                continue
            else:
                break

    print('#{} {}'.format(t,cnt)) 