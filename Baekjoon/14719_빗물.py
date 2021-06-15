H, W = map(int, input().split())
blocks = list(map(int, input().split()))
result = 0
for i in range(1, W - 1):
    maxLeft = max(blocks[:i])
    maxRight = max(blocks[i+1:])
    if min(maxLeft, maxRight) > blocks[i]:
        result += (min(maxLeft, maxRight) - blocks[i])
print(result)