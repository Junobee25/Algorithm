n = int(input())

arr = [64,32,16,8,4,2,1]

result = 0
cnt = 0

for i in range(len(arr)):
    if arr[i] > n:
        continue
    
    else:
        if result + arr[i] > n:
            continue
        
        result += arr[i]
        cnt += 1
        
    if result == n:
        print(cnt)
        break