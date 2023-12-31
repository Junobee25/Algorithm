def solution(record):
    info_list = []
    info_dict = {}
    count_dict = {}
    answer = []
    enter_view = "님이 들어왔습니다."
    leave_view = "님이 나갔습니다."
    
    for i in record:
        tmp = i.split(" ")
        if (tmp[0] != "Change"):
            info_list.append(tmp[1])
        
        if tmp[0] == "Enter":
            info_dict[tmp[1]] = tmp[2]
            count_dict[tmp[1]] = 0
            
        if tmp[0] == "Change":
            info_dict[tmp[1]] = tmp[2]
        
    for i in info_list:
        if count_dict[i] == 0:
            answer.append(info_dict[i] + enter_view)
            count_dict[i] += 1
            continue
        if count_dict[i] == 1:
            answer.append(info_dict[i] + leave_view)
            count_dict[i] = 0
    
    return answer