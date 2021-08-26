def solution(table, languages, preference):
    language_table = {}
    result = []
    max_point = float('-inf')
    for elm in table:
        elm = elm.split(" ")
        company, language = elm[0], elm[1:]
        language_table[company] = language
    for company, language_list in language_table.items():
        point = 0
        for idx, language in enumerate(languages):
            if language in language_list:
                point += (5 - language_list.index(language)) * preference[idx]
        if point > max_point:
            max_point = point
            result = [company]
        elif point == max_point:
            max_point = point
            result.append(company)
    return sorted(result)[0]

if __name__ == "__main__":
    print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5]))
    print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7,5]))