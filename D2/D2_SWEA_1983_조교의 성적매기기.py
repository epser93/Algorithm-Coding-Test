T=int(input())
grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
for k in range(T):
    student_num, student_index = map(int,input().split())
    student_point = []
    new_point =[]
    for i in range(student_num):
        student_point.append(list(map(int,input().split())))
        new_point.append(student_point[i][0] *0.35 + student_point[i][1] * 0.45 + student_point[i][2] * 0.2)

    rev_list=sorted(new_point,reverse=True)
    rank = rev_list.index(new_point[student_index-1])

    for j in range(10):
        if rank >= (0.1 * j * student_num) and rank < (0.1 * (j+1) *student_num):
            print(f'#{k+1} {grade[j]}')
        

