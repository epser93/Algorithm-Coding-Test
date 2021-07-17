numbers = [[] for _ in range(8)]
numDict = {
    '0' : ["***", "* *", "* *", "* *", "***"],
    '1' : ["  *", "  *", "  *", "  *", "  *"],
    '2' : ["***", "  *", "***", "*  ", "***"],
    '3' : ["***", "  *", "***", "  *", "***"],
    '4' : ["* *", "* *", "***", "  *", "  *"],
    '5' : ["***", "*  ", "***", "  *", "***"],
    '6' : ["***", "*  ", "***", "* *", "***"],
    '7' : ["***", "  *", "  *", "  *", "  *"],
    '8' : ["***", "* *", "***", "* *", "***"],
    '9' : ["***", "* *", "***", "  *", "***"]
}
for _ in range(5):
    words = input()
    temp = ""
    for idx, elm in enumerate(words):
        if idx == len(words)-1:
            numbers[idx // 4].append(temp+words[-1])
        if idx != 0 and (idx+1) % 4 == 0:
            numbers[idx // 4].append(temp)
            temp = ""
            continue
        temp += elm

result = ""
for number in numbers:
    for key, value in numDict.items():
        if number == value:
            result += key
            break
    else:
        if number != []:
            print("BOOM!!")
            exit()

number = int(result)
if number % 6:
    print("BOOM!!")
else:
    print("BEER!!")