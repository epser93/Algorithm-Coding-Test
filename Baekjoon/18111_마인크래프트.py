import sys
input = sys.stdin.readline
N, M, inventory = map(int, input().split())
lands = [list(map(int, input().split())) for _ in range(N)]
max_heights = max(map(max, lands))
min_heights = min(map(min, lands))
min_time = float('inf')
result_height = min_heights

for target_height in range(min_heights, max_heights+1):
    time = 0
    temp_inventory = 0
    for row in range(N):
        for col in range(M):
            diff_height = target_height - lands[row][col]
            if diff_height > 0:
                temp_inventory -= diff_height * 1
                time += diff_height * 1
            elif diff_height < 0:
                time += abs(diff_height) * 2
                temp_inventory += abs(diff_height) * 1
    if inventory + temp_inventory >= 0:
        if time <= min_time:
            min_time = time
            result_height = target_height
print(min_time, result_height)