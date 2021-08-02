def solution(price, money, count):
    fee = 0
    for i in range(count):
        fee += price * (i + 1)
    return fee - money if fee > money else 0

if __name__ == "__main__":
    print(solution(3, 20, 4))