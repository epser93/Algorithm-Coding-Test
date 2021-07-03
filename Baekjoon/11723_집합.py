import sys

def init():
    numDict = {}
    for i in range(1, 21):
        numDict[i] = 0
    return numDict    

def add(num):
    numDict[num] = 1

def remove(num):
    numDict[num] = 0

def check(num):
    if numDict.get(num):
        print(numDict[num])
    else:
        print(0)

def toggle(num):
    if numDict.get(num):
        numDict[num] = 0
    else:
        numDict[num] = 1

def all():
    for i in range(1, 21):
        numDict[i] = 1

def empty():
    for i in range(1, 21):
        numDict[i] = 0

input = sys.stdin.readline
numDict = init()
for _ in range(int(input())):
    command = input().split()
    if command[0] == "add":
        add(int(command[1]))
    elif command[0] == "remove":
        remove(int(command[1]))
    elif command[0] == "check":
        check(int(command[1]))
    elif command[0] == "toggle":
        toggle(int(command[1]))
    elif command[0] == "all":
        all()
    else:
        empty()
