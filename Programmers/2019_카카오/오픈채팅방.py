def change(id, afterName):
    for idx in resultIdx[id][1:]:
        result[idx] = result[idx].replace(resultIdx[id][0], afterName)
    resultIdx[id][0] = afterName
    return

def solution(records):
    global result, resultIdx
    resultIdx = {}
    result = []
    idx = 0
    for record in records:
        record = record.split()
        mode, id = record[0], record[1]
        if mode == "Enter":
            name = record[2]
            if resultIdx.get(id) == None:
                resultIdx[id] = [name, idx]
            else:
                if resultIdx[id][0] != name:
                    change(id, name)
                resultIdx[id].append(idx)
            idx += 1
            result.append(f"{name}님이 들어왔습니다.")
        elif mode == "Leave":
            result.append(f"{resultIdx[id][0]}님이 나갔습니다.")
            resultIdx[id].append(idx)
            idx += 1
        elif mode == "Change":
            name = record[2]
            change(id, name)
    return result

if __name__ == "__main__":
    print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))

