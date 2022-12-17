def solution(s):
    answer = 0
    t = ["",0,0]
    for i in s:
        if t[0] == "": # 빈 문자열이면
            t[0]  = i   
            t[1] += 1
        else:          # 빈 문자열이 아니면
            if t[0] == i: # 다음 문자와 처음 문자가 같으면 + 1 다르면 t[2] +1 을 함으로써 t[1] == t[2] 만든 후 answer 값을 증가
                t[1] += 1
            else:
                t[2] += 1
            if t[1] == t[2]: # 갯수가 다르면 처음 else 문 반복 갯수가 같으면 answer + 1 
                answer += 1
                t = ["",0,0] # 초기화 - 배열
    if t != ["",0,0]:        # 문자열 2개
        answer += 1
    return answer