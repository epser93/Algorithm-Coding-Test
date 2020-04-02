for t in range(1,int(input())+1):
    word = input()
    for i in range(len(word)//2):
        if (word[i] !='?' and word[len(word)-1-i]!= '?') and word[i] != word[len(word)-1-i]:
            print('#{} {}'.format(t,'Not exist'))
            break
    else: 
        print('#{} {}'.format(t,'Exist'))