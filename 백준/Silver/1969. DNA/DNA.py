import sys

input = sys.stdin.readline

n, m = map(int,input().split())


matrix = [list(input().strip()) for _ in range(n)]


result = ""
result_cnt = 0
for i in range(m):
    alpa_dict = {}
    for j in range(n):
        if matrix[j][i] in alpa_dict:
            alpa_dict[matrix[j][i]] += 1
        else:
            alpa_dict[matrix[j][i]] = 1
    
    temp_key = ""
    temp_value = 0
    
    for k in alpa_dict.keys():
        if alpa_dict[k] > temp_value:
            temp_key = k
            temp_value = alpa_dict[k]
            
        if alpa_dict[k] == temp_value:
            temp_key = min(k, temp_key)
    
    result += temp_key
    
    for k in alpa_dict.keys():
        if k != temp_key:
            result_cnt += alpa_dict[k]

print(result)
print(result_cnt)