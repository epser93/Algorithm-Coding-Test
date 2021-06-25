N = int(input())
arr = list(map(int, input().split()))

prev = arr[0]
chk = []
for i in range(1, len(arr)):
    if arr[i] > prev:
        chk.append('+')
    else:
        chk.append('-')
    prev = arr[i]
print(chk)
point = 0
for i in range(len(chk)-1):
    if i == 0 and chk[0] == "-":
        print("NO")
        break
    if chk[i] == "+" and chk[i+1] == "-":
        point += 1

if point > 1:
    print("NO")
else:
    print("YES")