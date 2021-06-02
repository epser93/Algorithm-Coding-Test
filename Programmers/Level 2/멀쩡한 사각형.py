import math

def solution(w, h):
    return w * h - (w + h - math.gcd(w, h))

if __name__ == "__main__":
    print(solution(8, 12))