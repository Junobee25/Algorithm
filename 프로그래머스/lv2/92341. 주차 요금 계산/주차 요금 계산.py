# 문자열 공백으로 나누기
# 기본시간 기본 요금 단위시간 분 단위 요금
# 기본시간 초과시 몇분당 얼마 누적

def solution(fees, records):
    tmp = []
    # 문자열 분리
    for i in range(len(records)):
        records[i] = records[i].split(' ')
    
    # 시간 계산
    for i in range(len(records)):
        records[i][0] = int(records[i][0][:2])*60 + int(records[i][0][3:])
    
    # 미리 정렬하기 입차 출차 순이므로 순방향으로 조건 찾아야 쉬울거 같음 
    records.sort(key = lambda x : (x[1], x[0]))
    
    # 첫번째 입차 배열 미리 tmp에 넣어 두기
    tmp.append(records[0])
    
    # 2번째 인덱스부터 탐색하여 이전 배열과의 입차 출차 차이 + IN // OUT 구분 하기
    for i in range(1,len(records)):
        
        # 같은 차량 번호 일 때
        if records[i][1] == tmp[-1][1]:
            
            # 현재 OUT일 때 계산해서 이전 배열에 갱신 하기
            if records[i][2] == 'OUT':
                tmp[-1][0] = abs(tmp[-1][0]-records[i][0])
                tmp[-1][2] = 'OUT'
            # 현재 IN일 때 계산하여 이전 배열에 갱신 하기
            else:
                tmp[-1][0] = abs(tmp[-1][0]-records[i][0])
                tmp[-1][2] = 'IN'
        # 다른 차량 번호 일 때 배열 새로 넣기
        else:
            tmp.append(records[i])
    
    # 마지막 기록이 IN 일 때 23:59에서 현재 시간 빼주기
    for i in range(len(tmp)):
        if tmp[i][2] == 'IN':
            tmp[i][0] = 1439-tmp[i][0]

    answer = [0]*len(tmp)
    
    
    # 주차 요금 계산
    for i in range(len(tmp)):

        if tmp[i][0] <= fees[0]:
            answer[i] = fees[1]
        else:
            calcul = tmp[i][0]-fees[0]
            # 나누어 떨어지지 않으면 올림 하는 계산
            if (calcul) % fees[2] != 0:
                calcul = (tmp[i][0]-fees[0]) + (fees[2] - (calcul % fees[2]))
                answer[i] = fees[1] + ((calcul)//fees[2]) * fees[3]
            else:
                answer[i] = fees[1] + ((calcul)//fees[2]) * fees[3]
                
    return answer