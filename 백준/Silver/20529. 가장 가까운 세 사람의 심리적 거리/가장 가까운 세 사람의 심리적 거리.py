import sys
from itertools import combinations
input = sys.stdin.readline

t = int(input())

def calculator_distance(mbti, compare_mbti):
    cnt = 0
    
    for i in range(4):
        if mbti[i] != compare_mbti[i]:
            cnt += 1
            
    return cnt

for _ in range(t):
    n = int(input())
    arr = list(map(str, input().split()))
    
    if n > 32:
        print(0)
    else:
        min_value = 13
        for sub_list in combinations(arr, 3):
            temp = 0
            temp += calculator_distance(sub_list[0], sub_list[1]) + calculator_distance(sub_list[1], sub_list[2]) + calculator_distance(sub_list[0], sub_list[2])
            if min_value > temp:
                min_value = temp
                
        print(min_value)
        