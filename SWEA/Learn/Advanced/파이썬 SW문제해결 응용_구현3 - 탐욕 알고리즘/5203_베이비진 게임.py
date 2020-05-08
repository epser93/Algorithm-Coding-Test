class babygin:
    def __init__(self):
        self.before = {}
    def result(self, number):
        before = self.before

        if number in before:
            before[number] += 1
            if before[number] == 3:
                return True
        else:
            before[number] = 1
            if before.get(number-1) and before.get(number+1):
                return True
            elif before.get(number-1) and before.get(number-2):
                return True
            elif before.get(number+1) and before.get(number+2):
                return True
        return False

for t in range(1,int(input())+1):
    number = list(map(int,input().split()))
    p1 = babygin()
    p2 = babygin()

    for i in range(len(number)):
        if i % 2 == 0: # 홀수 번째 >> 1번한테
            a = p1.result(number[i])
            if a == True:
                print('#{} 1'.format(t))
                break
        else: # 짝수 번쨰 >> 2번 한테
            b = p2.result(number[i])
            if b == True:
                print('#{} 2'.format(t))
                break
    else:
        print('#{} 0'.format(t))

