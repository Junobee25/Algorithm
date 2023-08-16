n,b = map(int,input().split())
arr = list(map(int,input().split()))

idx_dict = {}
count_dict = {}

number_arr = []


for i in range(n):
    if arr[i] not in count_dict:
        count_dict[arr[i]] = 1
    else:
        count_dict[arr[i]] += 1

for i in range(n):
    if arr[i] not in idx_dict:
        idx_dict[arr[i]] = i
    else:
        pass
    
for i in range(n):
    number_arr.append((arr[i],count_dict[arr[i]],idx_dict[arr[i]]))
    
number_arr.sort(key = lambda x : (-x[1],x[2]))

for i in range(n):
    print(number_arr[i][0], end = ' ')