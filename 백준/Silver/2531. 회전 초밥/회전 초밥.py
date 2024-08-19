import sys

input = sys.stdin.readline

N, d, k, c = map(int, input().split())

s_list = []

s_dict = {}

cnt = 0
result = 0

for _ in range(N):
    s = int(input())
    s_list.append(s)

idx = 0

while idx <= N + k - 1:
    i = idx % len(s_list)
    
    if idx > k - 1:
        if s_dict[s_list[i - k]] == 1:
            del[s_dict[s_list[i - k]]]
        else:
            s_dict[s_list[i - k]] -= 1
            
        if s_list[i] not in s_dict:
            s_dict[s_list[i]] = 1
        else:
            s_dict[s_list[i]] += 1
            
        if c in s_dict:
            cnt = len(s_dict)
        else:
            cnt = len(s_dict) + 1
            
    elif idx < k - 1:
        if s_list[i] in s_dict:
            s_dict[s_list[i]] += 1
        else:
            s_dict[s_list[i]] = 1
            
    else:
        if s_list[i] in s_dict:
            s_dict[s_list[i]] += 1
        else:
            s_dict[s_list[i]] = 1
            
        if c in s_dict:
            cnt = len(s_dict)
        else:
            cnt = len(s_dict) + 1
    if cnt > result:
        result = cnt
    idx += 1
print(result)
            