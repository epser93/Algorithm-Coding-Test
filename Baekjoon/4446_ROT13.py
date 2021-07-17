while 1:
    try:
        sentences = input()
        vowel = "aiyeou" # 모음
        consonant = "bkxznhdcwgpvjqtsrlmf" # 자음
        result = ""
        for sentence in sentences:
            isUpper = False
            if sentence == " ":
                result += " "
                continue
            if sentence.isupper():
                isUpper = True
            word = sentence.lower()
            if word in vowel:
                idx = vowel.index(word)
                word = vowel[(idx+3) % len(vowel)]
            elif word in consonant:
                idx = consonant.index(sentence.lower())
                word = consonant[(idx+10) % len(consonant)]
            if isUpper:
                result += word.upper()
            else:
                result += word
        print(result)
    except:
        break