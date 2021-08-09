def getDistance(pos1, pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

left = {
    'q' : (0, 0), 'w' : (0, 1), 'e' : (0, 2), 'r' : (0, 3), 't' : (0, 4),
    'a' : (1, 0), 's' : (1, 1), 'd' : (1, 2), 'f' : (1, 3), 'g' : (1, 4),
    'z' : (2, 0), 'x' : (2, 1), 'c' : (2, 2), 'v' : (2, 3)
}

right = {
    'y' : (0, 5), 'u' : (0, 6), 'i' : (0, 7), 'o' : (0, 8), 'p' : (0, 9),
    'h' : (1, 5), 'j' : (1, 6), 'k' : (1, 7), 'l' : (1, 8),
    'b' : (2, 4), 'n' : (2, 5), 'm' : (2, 6)
}
position = input().split()
leftPosition, rightPosition = left[position[0]], right[position[1]]
words = input()
result = 0
for word in words:
    if left.get(word):
        result += getDistance(leftPosition, left[word]) + 1
        leftPosition = left[word]
    else:
        result += getDistance(rightPosition, right[word]) + 1
        rightPosition = right[word]
print(result)