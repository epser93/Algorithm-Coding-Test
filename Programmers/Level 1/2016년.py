def solution(a, b):
    WEEK = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    monthDay = {
        1 : 31,
        2 : 29,
        3 : 31,
        4 : 30,
        5 : 31,
        6 : 30,
        7 : 31,
        8 : 31,
        9 : 30,
        10 : 31,
        11 : 30,
        12 : 31,
    }
    day = 0
    for month in range(1, a):
        day += monthDay[month]
    day += (b - 1)
    return WEEK[day % 7]

if __name__ == "__main__":
    print(solution(5, 24))

