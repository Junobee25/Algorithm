"""
<단품 -> 코스요리 재구성>
1. 이전에 가장 많이 함께 주문한 단품메뉴를 코스요리로 구성
2. 최소 2가지 이상의 단품 메뉴
3. 최소 2명이상에게 주문된 단품메뉴
"""
from itertools import combinations

def solution(orders, course):
    result = {}
    answer = []

    for order in orders:
        for cnt in course:
            if len(order) >= cnt:
                order_case = list(combinations(order,cnt))
                for case in order_case:
                    case = list(case)
                    case.sort()
                    case = "".join(case)
                    if case in result:
                        result[case] += 1
                    else:
                        result[case] = 1
    
    for cnt in course:
        max_value = 0
        for ele in result:
            if len(ele) == cnt and result[ele] >= 2 and result[ele] >= max_value:
                max_value = result[ele]
        
        for ele_t in result:
            if len(ele_t) == cnt and result[ele_t] >= 2 and result[ele_t] >= max_value:
                answer.append(ele_t)
    answer.sort()
    
    return answer