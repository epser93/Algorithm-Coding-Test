N = int(input())
trees = list(map(int, input().split()))
grow = list(map(int, input().split()))
result = 0
treeStatus = []
for i in range(N):
    treeStatus.append([trees[i], grow[i]])
treeStatus.sort(key=lambda x : x[1], reverse=True)
for i in range(N):
    tree, grow = treeStatus.pop()
    result += (tree + grow * i)
print(result)