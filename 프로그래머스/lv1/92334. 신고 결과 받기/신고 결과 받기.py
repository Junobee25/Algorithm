def solution(id_list, report, k):
    # id_list의 예측 결과 값
    answer = [0]*len(id_list)
    
    # 누가 몇번 지목 당했는지에 대한 딕셔너리
    id_dict = {}
    
    # 시간초과 해결하기 위해서 idx를 딕셔너리에 추가
    idx_dict = {}
    
    for i in range(len(id_list)):
        idx_dict[id_list[i]] = i
        
    # 누가 몇번 지목 당했는지 초기화
    for i in id_list:
        id_dict[i] = 0
    # 중복처리는 set을 이용하면 될 것 같다고 생각 함(어차피 한명이 한사람만 지목하므로)
    new_report = list(set(report))
    
    # 문자열 처리 하기 위해 split 사용
    for i in range(len(new_report)):
        new_report[i] = new_report[i].split(' ')
        # 지목 당한 횟수 count
        id_dict[new_report[i][1]] += 1
    
    # 딕셔너리 key(지목당한 사람), value(몇번) 모두 필요 함
    for key, value in id_dict.items(): # id_list의 길이 최대값 1000
        # k번 이상 지목 되면 메일 전송
        if value >= k:
            
            # c[0] => 누가 c[1] => 누굴 지목 함
            for c in new_report: # new_report의 최대 길이 200,000
                if key == c[1]:
                    
                    # index함수 O(n) => id_list의 최대 값 O(1000)
                    # answer[id_list.index(c[0])] += 1
                    
                    # 딕셔너리 키에 대한 인덱스를 바로 추출 O(1)
                    answer[idx_dict[c[0]]] += 1
        
    return answer