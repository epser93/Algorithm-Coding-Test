alphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
sentence = input()
idx = 0
temp = ""
result = 0
while idx < len(sentence):
    if sentence[idx:idx+3] in alphabets:
        idx += 3
    elif sentence[idx:idx+2] in alphabets:
        idx += 2
    else:
        idx += 1
    result += 1
print(result)