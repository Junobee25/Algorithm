T = int(input())
arr = []
new_list = []
for i in range(T):
    v = input()
    arr.append((v,len(v)))
arr.sort(key = lambda x: (x[1],x[0]))
for i in range(T):
    if arr[i][0] in new_list:
        pass
    else:
        new_list.append(arr[i][0])
for j in new_list:
    print(j)
