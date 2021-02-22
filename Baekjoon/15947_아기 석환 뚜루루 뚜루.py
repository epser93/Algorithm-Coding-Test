n = int(input())
lyric = "baby sukhwan tururu turu very cute tururu turu in bed tururu turu baby sukhwan".split()

lengthOfLyric = len(lyric)

loopNum = (n-1) // lengthOfLyric
lyricPosition = (n-1) % lengthOfLyric

if 'turu' in lyric[lyricPosition]:
    lyric[lyricPosition] += 'ru' * loopNum
    k = lyric[lyricPosition].count('ru')
    if k >= 5:
        print("tu+ru*" + str(k))
    else:
        print(lyric[lyricPosition])
else:
    print(lyric[lyricPosition])