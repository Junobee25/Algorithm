def solution(lottos, win_nums):
    answer = []
    rank = {6 : '1', 5 : '2', 4 : '3', 3 : '4', 2 : '5', 1 : '6', 0 : '6'}
    collect_num = 0
    zero = 0
    for i in lottos:
        if (i == 0):
            zero += 1
        elif (i in win_nums):
            collect_num += 1
            
    max_rank = collect_num + zero
    
    answer.append(int(rank[max_rank]))
    answer.append(int(rank[collect_num]))
    
    return answer