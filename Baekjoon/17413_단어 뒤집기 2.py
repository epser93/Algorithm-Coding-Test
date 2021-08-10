S = input()
tagChk = False
temp = ""
wordArr = []
for s in S:
    if s == "<":
        tagChk = True
        if temp:
            wordArr.append(temp)
            temp = "" 
    if s == ">":
        wordArr.append(temp+s)
        temp = ""
        tagChk = False
        continue
    if tagChk:
        temp += s
        continue
    temp += s
if temp:
    wordArr.append(temp)
result = ""
for word in wordArr:
    if word[0] == "<":
        result += word
        continue
    temp = []
    for w in word.split():
        temp.append(w[::-1])
    result += ' '.join(temp)
print(result)