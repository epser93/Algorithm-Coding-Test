def dn(n):
    result = n
    n = str(n)
    for i in range(len(n)):
        result += int(n[i])
    return result

def makeConstructorDict():
    constructorDict = {}
    for i in range(1, 10001):
        constructorDict[dn(i)] = i
    return constructorDict

constructorDict = makeConstructorDict()
for i in range(1, 10001):
    if not constructorDict.get(i):
        print(i)