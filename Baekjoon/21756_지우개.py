N = int(input())
arr = [x for x in range(1, N+1)]
cnt = 0
while len(arr) != 1:
    for i in range(0, len(arr), 2):
        arr[i] = 0
    arr = [x for x in arr if x != 0]
print(arr[0])