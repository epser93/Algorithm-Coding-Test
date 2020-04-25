T = int(input())
for t in range(T):
    word = input()
    i = 1
    while 1:
        if word[0:i] == word[i:2*i]:
            break
        i += 1
    print(f'#{t+1} {i}')