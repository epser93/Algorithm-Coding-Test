def solution(sentences):
    answer = 0
    sentenceLength = len(sentences)
    for i in range(sentenceLength):
        stack = []
        sentence = sentences[i:] + sentences[:i]
        stackLength = 0
        for idx in range(sentenceLength):
            if stackLength == 0:
                if sentence[idx] == "]" or sentence[idx] == ")" or sentence[idx] == '}':
                    stackLength = "BREAK"
                    break
                stack.append(sentence[idx])
                stackLength += 1
            else:
                if stack[-1] == "(":
                    if sentence[idx] == ")":
                        stack.pop()
                        stackLength -= 1
                    elif sentence[idx] == "}" or sentence[idx] == "]":
                        break
                    else:
                        stack.append(sentence[idx])
                        stackLength += 1
                elif stack[-1] == "{":
                    if sentence[idx] == "}":
                        stack.pop()
                        stackLength -= 1
                    elif sentence[idx] == ")" or sentence[idx] == "]":
                        break
                    else:
                        stack.append(sentence[idx])
                        stackLength += 1
                elif stack[-1] == "[":
                    if sentence[idx] == "]":
                        stack.pop()
                        stackLength -= 1
                    elif sentence[idx] == "}" or sentence[idx] == ")":
                        break
                    else:
                        stack.append(sentence[idx])
                        stackLength += 1
                else:
                    print('------------------------')
        if idx == sentenceLength - 1 and stackLength == 0:
            answer += 1

    return answer

if __name__ == "__main__":
    print(solution("[](){}"))
    print(solution("}]()[{"))
    print(solution("[)(]"))
    print(solution("}}}"))
    print(solution("((("))
    print(solution("(())("))
    print(solution("]"))