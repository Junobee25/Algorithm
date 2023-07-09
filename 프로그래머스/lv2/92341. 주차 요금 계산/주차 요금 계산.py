# 문자열 공백으로 나누기
# 기본시간 기본 요금 단위시간 분 단위 요금
# 기본시간 초과시 몇분당 얼마 누적

# 
def solution(fees, records):
    tmp = []

    for i in range(len(records)):
        records[i] = records[i].split(' ')
    for i in range(len(records)):
        records[i][0] = int(records[i][0][:2])*60 + int(records[i][0][3:])
    
    records.sort(key = lambda x : (x[1], x[0]))
    tmp.append(records[0])
    
    for i in range(1,len(records)):
        if records[i][1] == tmp[-1][1]:
            if records[i][2] == 'OUT':
                tmp[-1][0] = abs(tmp[-1][0]-records[i][0])
                tmp[-1][2] = 'OUT'
            else:
                tmp[-1][0] = abs(tmp[-1][0]-records[i][0])
                tmp[-1][2] = 'IN'
        else:
            tmp.append(records[i])

    for i in range(len(tmp)):
        if tmp[i][2] == 'IN':
            tmp[i][0] = 1439-tmp[i][0]

    answer = [0]*len(tmp)
    
    for i in range(len(tmp)):

        if tmp[i][0] <= fees[0]:
            answer[i] = fees[1]
        else:
            calcul = tmp[i][0]-fees[0]
            if (calcul) % fees[2] != 0:
                calcul = (tmp[i][0]-fees[0]) + (fees[2] - (calcul % fees[2]))
                answer[i] = fees[1] + ((calcul)//fees[2]) * fees[3]
            else:
                answer[i] = fees[1] + ((calcul)//fees[2]) * fees[3]
    return answer