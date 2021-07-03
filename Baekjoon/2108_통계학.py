import sys
from collections import Counter

def mode(nums, lenOfNums):
    countOfNums = Counter(nums).most_common()
    if lenOfNums > 1 and countOfNums[0][1] == countOfNums[1][1]:
        return countOfNums[1][0]
    return countOfNums[0][0]

input = sys.stdin.readline
nums = []
numberDict = {}
for _ in range(int(input())):
    num = int(input())
    nums.append(num)
nums.sort()
lenOfNums = len(nums)

print(int(round(sum(nums)/lenOfNums,0))) 
print(nums[lenOfNums // 2]) 
print(mode(nums, lenOfNums))
print(nums[-1] - nums[0])