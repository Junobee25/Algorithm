def solution(s):
    answer = []
    
    s = s[1:len(s)-1]
    s = s.split(",")
    
    pre_list = []
    tmp_list = []

    for i in range(len(s)):
        tmp_number = ""
        for j in range(len(s[i])):
            if (s[i][j] == "}"):
                tmp_list.append(int(tmp_number))
                tmp_number = ""
                pre_list.append(tmp_list)
                tmp_list = []
                
            if (s[i][j].isdigit()):
                tmp_number += s[i][j]
        if (tmp_number != ""):
            tmp_list.append(int(tmp_number))
                
                
    pre_list.sort(key=lambda x: (len(x)))

    
    for i in range(len(pre_list)):
        for j in range(len(pre_list[i])):
            if (pre_list[i][j] in answer):
                continue
            else:
                answer.append(pre_list[i][j])
    
    return answer