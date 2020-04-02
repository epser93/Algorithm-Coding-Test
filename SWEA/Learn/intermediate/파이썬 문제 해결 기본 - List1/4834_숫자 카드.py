T = int(input())
for j in range(T):
    n = int(input())
    num = int(input())
    num_list = []
    num_dic ={}
    for i in range(n):
        num_list.append(num % 10)
        num = num // 10
    for k in num_list:
        if k not in num_dic:
            num_dic[k] = 1
        else:
            num_dic[k] += 1
    sort_dict = sorted(num_dic.items(),reverse=True)
    for key, value in sort_dict:
        if value == max(num_dic.values()):
            print('#{} {} {}'.format(j+1, key, value))
            break