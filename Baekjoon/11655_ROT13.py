sentences = input()
result = ""
for elm in sentences:
    ascii_num = ord(elm)
    new_ascii_num = ascii_num + 13
    if 65 <= ascii_num <= 90:
        if new_ascii_num > 90:
            new_ascii_num = 64 + new_ascii_num - 90
        elif new_ascii_num > 122:
            new_ascii_num = 96 + new_ascii_num - 122
        result += chr(new_ascii_num)
    elif 97 <= ascii_num <= 122:
        if new_ascii_num > 122:
            new_ascii_num = 96 + new_ascii_num - 122
        result += chr(new_ascii_num)
    else:
        result += elm
        continue
print(result)