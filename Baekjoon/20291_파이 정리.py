n = int(input())
file_dict = {}
for _ in range(n):
    file = input().split('.')[-1]
    if not file_dict.get(file):
        file_dict[file] = 1
    else:
        file_dict[file] += 1
for file in sorted(file_dict):
    print(file, file_dict[file])