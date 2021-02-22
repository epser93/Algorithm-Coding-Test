numOfSignal, lengthOfRoad = map(int, input().split())
signalInfo = [list(map(int, input().split())) for _ in range(numOfSignal)]

position = 0
time = 0
signalIdx = 0
signal = signalInfo[signalIdx]
while position != lengthOfRoad:
    time += 1
    position += 1
    if position == signal[0]:
        if time % (signal[1] + signal[2]) <= signal[1]:
            time += (signal[1] - time % (signal[1] + signal[2]))
        signalIdx += 1
        if signalIdx < numOfSignal:
            signal = signalInfo[signalIdx]

print(time)