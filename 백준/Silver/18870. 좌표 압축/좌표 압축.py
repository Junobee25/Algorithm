import copy

number_dict = {}

n = int(input())

temp = list(map(int,input().split()))

arr = copy.deepcopy(temp)

temp = list(set(temp))
temp.sort()

for i in range(len(temp)):
    if temp[i] not in number_dict:
        number_dict[temp[i]] = i
    else:
        pass
    
for i in range(len(arr)):
    print(number_dict[arr[i]], end = ' ')