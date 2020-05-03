def solution(participant, completion):
    participant_dic={}
    completion_dic={}
    for people in participant:
        if people not in participant_dic:
            participant_dic[people] = 1
        else:
            participant_dic[people] += 1

    for people2 in completion:
        if people2 not in completion_dic:
            completion_dic[people2] = 1
        else:
            completion_dic[people2] += 1

    for key,value in participant_dic.items():
        if key not in completion_dic or value - completion_dic[key] == 1:
            return key