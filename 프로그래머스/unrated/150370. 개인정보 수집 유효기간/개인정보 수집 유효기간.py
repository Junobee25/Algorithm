def solution(today, terms, privacies):
    answer = []
    dic = {}
    ymd = today.split('.')
    
    # 체크할 날짜
    end = int(ymd[0])*336 + int(ymd[1])*28 + int(ymd[2])
    # ex) A : 6*28
    for i in terms:
        dic[i.split(' ')[0]] = int(i.split(' ')[1])*28
    
    # 시작날짜
    for i in range(len(privacies)):
        ym_list = privacies[i].split('.')
        d,available = ym_list[2].split(' ')
        start = int(ym_list[0])*336 + int(ym_list[1])*28 + int(d)
        if end-start >= dic[available]:
            answer.append(i+1)
            
    answer.sort()
    return answer

