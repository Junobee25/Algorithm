## 외판원 순회 2
from itertools import permutations
N = int(input())

W = []

for _ in range(N):
    W.append(list(map(int,input().split())))

result = 100000001

for i in range(N):
    arr = [k for k in range(N) if not k == i]
    nPr_list = list(permutations(arr, len(arr)))
    for j in range(len(nPr_list)):
        start_point = i
        end_point = i
        temp_result = 0
        flag = True
        for k in range(len(nPr_list[j])):
            if (W[start_point][nPr_list[j][k]] == 0):
                flag = False
                break 
            temp_result += W[start_point][nPr_list[j][k]]
            start_point = nPr_list[j][k]
            
        if (W[start_point][end_point] == 0):
            flag = False
        if (W[start_point][end_point] != 0):
            temp_result += W[start_point][end_point]
        if (result > temp_result and flag):
            result = temp_result
            
print(result)