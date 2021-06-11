dic = {}
for num in input():
    if num == "9":
        num = "6"
    if not dic.get(num):
        dic[num] = 1
    else:
        dic[num] += 1
sixNine = dic.get('6')
if sixNine:
    if sixNine % 2:
        sixNineCnt = sixNine // 2 + 1
    else:
        sixNineCnt = sixNine // 2 
    dic['6'] = 0
else:
    sixNineCnt = 0
maxValue = max(dic.values())
print(max(sixNineCnt, maxValue))