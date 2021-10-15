N = int(input())
i = 1
summ = 1
while 1:
    if summ >= N:
        break
    i += 1
    summ += (6*(i-1))
print(i)