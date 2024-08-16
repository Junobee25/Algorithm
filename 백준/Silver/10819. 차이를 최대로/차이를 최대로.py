from itertools import permutations

n = int(input())

arr = list(map(int,input().split()))
result = 0

for sub_list in list(permutations(arr, len(arr))):
    temp_result = 0
    for i in range(len(sub_list) - 1):
        temp_result += abs(sub_list[i] - sub_list[i + 1])
        
    if temp_result > result:
        result = temp_result
        
print(result)