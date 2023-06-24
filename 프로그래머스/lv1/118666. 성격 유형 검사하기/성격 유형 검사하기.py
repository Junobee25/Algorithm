def solution(survey, choices):
    answer = ''
    result_dict = {'R': 0,'T': 0,
                    'C' : 0, 'F' : 0,
                    'J' : 0, 'M' : 0,
                    'A' : 0, 'N' : 0}
    
    for i in range(len(survey)):
        if choices[i] == 4:
            result_dict[survey[i][0]] += 0
            result_dict[survey[i][1]] += 0
        elif choices[i] == 5:
            result_dict[survey[i][1]] += 1
        elif choices[i] == 6:
            result_dict[survey[i][1]] += 2
        elif choices[i] == 7:
            result_dict[survey[i][1]] += 3
        elif choices[i] == 3:
            result_dict[survey[i][0]] += 1
        elif choices[i] == 2:
            result_dict[survey[i][0]] += 2
        elif choices[i] == 1:
            result_dict[survey[i][0]] += 3
            
    if result_dict['R'] >= result_dict['T']:
        answer += 'R'
    else:
        answer += 'T'
    
    if result_dict['C'] >= result_dict['F']:
        answer += 'C'
    else:
        answer += 'F'
    
    if result_dict['J'] >= result_dict['M']:
        answer += 'J'
    else:
        answer += 'M'
        
    if result_dict['A'] >= result_dict['N']:
        answer += 'A'
    else:
        answer += 'N'
    return answer