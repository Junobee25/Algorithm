def solution(dartResult):
    number_list = []
    tmp_alpha = ''
    
    for i in dartResult:
        if i.isdigit():
            tmp_alpha += i
        if i.isalpha():
            if i == "S":
                tmp_alpha = int(tmp_alpha)**1
            if i == "D":
                tmp_alpha = int(tmp_alpha)**2
            if i == "T":
                tmp_alpha = int(tmp_alpha)**3
                
            number_list.append(tmp_alpha)
            tmp_alpha = ''
            
        if i == "#":
            number_list[-1] = number_list[-1] * -1
            
        if i == "*":
            if len(number_list) == 1:
                number_list[0] = number_list[0] * 2
            if len(number_list) == 2:
                number_list[0] = number_list[0] * 2
                number_list[1] = number_list[1] * 2
            if len(number_list) == 3:
                number_list[1] = number_list[1] * 2
                number_list[2] = number_list[2] * 2
                
    answer = sum(number_list)
    return answer