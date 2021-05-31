def solution(s):
    return (len(s) == 4 or len(s) == 6) and s.isdecimal() 

if __name__ == "__main__":
    print(solution("a234"))
    print(solution("1234"))