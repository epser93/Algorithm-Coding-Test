def find_word(word):
  global word_set, result
  for i in range(6):
    temp_word = ''
    if word[i] == '0':
      temp_word = word[:i] + '1' + word[i+1:]
    else:
      temp_word = word[:i] + '0' + word[i+1:]
    if word_set.get(temp_word):
      result += word_set.get(temp_word)
      return True
  return False

word_set = {
  '000000' : 'A', '001111' : 'B', '010011' : 'C', '011100' : 'D',
  '100110' : 'E', '101001' : 'F', '110101' : 'G', '111010' : 'H'
}

n = int(input())
words = input()
result = ''
for i in range(n):
  word = words[6*i:6*(i+1)]
  if word_set.get(word):
    result += word_set.get(word)
    continue
  if not find_word(word):
    print(i+1)
    break
else:
  print(result)