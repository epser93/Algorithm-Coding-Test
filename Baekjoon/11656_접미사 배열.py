import sys

input = sys.stdin.readline().rstrip
S = input()
arr = []
for i in range(len(S)): 
    arr.append(S[i:len(S)])
arr.sort()
for i in range(len(S)):
    print(arr[i])