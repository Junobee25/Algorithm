arr = input()
stick = 0
cnt = 0 
l = len(arr)
i = 0
while i < l:
    if arr[i] == '(' and arr[i+1] == ')':
        cnt += stick
        i += 2

    elif arr[i] == '(':
        stick += 1
        i += 1
    else :
        cnt += 1
        stick -= 1
        i += 1
        
print(cnt)