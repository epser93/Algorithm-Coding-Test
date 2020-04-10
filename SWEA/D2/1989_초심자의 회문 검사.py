T= int(input())
for t in range(T):
    word = input()
    new_word = ""
    for i in range(len(word)-1,-1,-1):
        new_word += word[i]
    if new_word == word:
        print(f'#{t+1} {1}')
    else:
        print(f'#{t+1} {0}')