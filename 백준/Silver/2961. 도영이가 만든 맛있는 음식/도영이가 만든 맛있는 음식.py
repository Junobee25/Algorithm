import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())

food_case = []

for _ in range(N):
    a, b = map(int,input().split())
    food_case.append((a,b))


result = float('inf')

for i in range(1, N + 1):

    for sub_list in combinations(food_case, i):
        m = 1
        a = 0
        for food_col in sub_list:
            m *= food_col[0]
            a += food_col[1]
            
        if abs(m - a) < result:
            result = abs(m - a)   
            
print(result)