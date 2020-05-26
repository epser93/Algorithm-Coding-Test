T = int(input())
for t in range(T):
    str1 = input()
    str2 = input()
    word_ = {}
    for word in str1:
        if word not in word_:
            word_[word] = 0

    for word2 in str2:
        if word2 in word_:
            word_[word2] += 1

    print('#{} {}'.format(t+1,max(word_.values())))