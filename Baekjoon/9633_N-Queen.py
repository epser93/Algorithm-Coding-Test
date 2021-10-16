def test(row, col, result):
    # 열 체크
    if col in result:
        return False
    # 대각 체크
    for rows, cols in enumerate(result):
        if abs(rows-row) == abs(cols-col):
            return False
    return True

def dfs(row, result):
    global cnt
    if row == N:
        cnt += 1
        return
    for col in range(N):
        if test(row, col, result):
            dfs(row+1, result+[col])

N = int(input())
cnt = 0
dfs(0, [])
print(cnt)