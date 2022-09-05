def find_time_num(number):
  min_number = '10000'
  for _ in range(4):
    if int(number) < int(min_number):
      min_number = number
    number = number[1:] + number[0]
  return min_number
    
number_set = set()
for i in range(1, 10):
  for j in range(1, 10):
    for k in range(1, 10):
      for l in range(1, 10):
        number = str(i*1000 + j*100 + k*10 + l)
        min_number = find_time_num(number)
        number_set.add(min_number)
number_set = sorted(number_set)

input_number = input().split()
a = input_number[0]+input_number[1]+input_number[2]+input_number[3]
input_number = find_time_num(input_number[0]+input_number[1]+input_number[2]+input_number[3])

print(number_set.index(input_number)+1)