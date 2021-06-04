def getVocab(str):
    visit = {}
    vocab = []
    for j in range(len(str)-1):
        token = str[j:j+2].upper()
        if token.isalpha():
            vocab.append(token)
            if visit.get(token):
                visit[token] += 1
            else:
                visit[token] = 1
    return set(vocab), visit

def getGyo(vocab1, vocab2, dict1, dict2):
    result = 0
    gyo = vocab1 & vocab2
    for elm in gyo:
        result += min(dict1[elm], dict2[elm])
    return result

def getHab(vocab1, vocab2, dict1, dict2):
    result = 0
    hab = vocab1 | vocab2
    for elm in hab:
        if dict1.get(elm) and dict2.get(elm):
            result += max(dict1[elm], dict2[elm])
        elif dict1.get(elm):
            result += dict1[elm]
        else:
            result += dict2[elm]
    return result

def getJacard(gyo, hab):
    if hab == 0:
        return 1
    return gyo / hab      

def solution(str1, str2):
    vocab1, dict1 = getVocab(str1)
    vocab2, dict2 = getVocab(str2)
    gyo, hab = getGyo(vocab1, vocab2, dict1, dict2), getHab(vocab1, vocab2, dict1, dict2)
    jacard = getJacard(gyo, hab)
    return int(jacard * 65536)

if __name__ == "__main__":
    print(solution("FRANCE", "french"))
    print(solution("handshake", "shake hands"))
    print(solution("aa1+aa2", "AAAA12"))
    print(solution("E=M*C^2", "e=m*c^2"))





def solution(str1, str2):
    answer = 0
    
    l1 = []
    l2 = []
    
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            frac = str1[i] + str1[i+1]
            l1.append(frac.lower())
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            frac = str2[i] + str2[i+1]
            l2.append(frac.lower())
    # print(l1)
    # print(l2)
    
    inter = 0
    union = 0
    done = []
    
    for j in range(len(l1)):
        target = l1[j]
        if target not in done:
            l1_c = l1.count(target)
            l2_c = l2.count(target)
            res = min(l1_c, l2_c)
            inter += res
            done.append(target)
    
    # print(inter)
    done = []
    for q in range(len(l2)):
        target = l2[q]
        if target not in done:
            l1_c = l1.count(target)
            l2_c = l2.count(target)
            res = max(l1_c, l2_c)
            union += res
            done.append(target)
            # print(done)
    
    for j in range(len(l1)):
        target = l1[j]
        if target not in done:
            l1_c = l1.count(target)
            l2_c = l2.count(target)
            res = max(l1_c, l2_c)
            union += res
            done.append(target)
    # print(union)
    
    if not l1 and not l2:
        answer = 65536
    else:
        answer = int(inter/union * 65536)
    return answer