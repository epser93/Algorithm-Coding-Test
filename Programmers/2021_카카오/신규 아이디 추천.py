def toLower(id):
    return id.lower()

def remove(id):
    possibleDict = ["-", "_", "."]
    new_id = ""
    for elm in id:
        if elm.isalpha() or elm.isalnum() or elm in possibleDict:
            new_id += elm
    return new_id

def removeContinualPunc(id):
    isPunc = False
    new_id = ""
    for elm in id:
        if isPunc and elm == '.':
            continue
        elif not isPunc and elm == '.':
            new_id += '.'
            isPunc = True
        else:
            isPunc = False
            new_id += elm
    return new_id

def removeFirstEndPunc(id):
    return id.strip(".")

def truncate(id):
    if len(id) >= 16:
        id = id[:15]
        return id.strip('.')
    else:
        return id

def solution(new_id):
    new_id = toLower(new_id)
    new_id = remove(new_id)
    new_id = removeContinualPunc(new_id)
    new_id = removeFirstEndPunc(new_id)
    if len(new_id) == 0:
        new_id += "a"
    new_id = truncate(new_id)

    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    return new_id

if __name__ == "__main__":
    print(solution("...!@BaT#*..y.abcdefghijklm"))
    print(solution("z-+.^."))
    print(solution("=.="))
    print(solution("123_.def"))
    print(solution("abcdefghijklmn.p"))