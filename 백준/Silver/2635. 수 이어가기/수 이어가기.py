n = int(input())

max_list = []
for i in range(1, n + 1):
    temp_list = [n]
    temp_list.append(i)
    
    idx = 1
    
    while True:
        k = temp_list[idx - 1] - temp_list[idx]
        if k < 0:
            break
        temp_list.append(k)
        idx += 1

    if len(max_list) < len(temp_list):
        max_list = temp_list
        
        

print(len(max_list))
for i in max_list:
    print(i, end=" ")