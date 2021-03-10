import sys

input = sys.stdin.readline

dayOfMonth = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
}
weeks = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
day = 0
x, y =map(int, input().split())

for i in range(1, x):
    day += dayOfMonth[i]
day += y

print(weeks[day % 7])