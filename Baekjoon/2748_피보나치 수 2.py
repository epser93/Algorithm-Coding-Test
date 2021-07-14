def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if not nums[n]:
        nums[n] = fibonacci(n-1) + fibonacci(n-2)
    return nums[n]

n = int(input())
nums = [0] * 91
print(fibonacci(n))