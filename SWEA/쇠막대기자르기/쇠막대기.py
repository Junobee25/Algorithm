T = int(input())

for test_case in range(1,T+1):
    arr = list(input())
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
        # 쇠막대기의 끝에 왜 cnt += 1 하는지 생각해보기 
        else :
            cnt += 1
            stick -= 1
            i += 1
        
    print('#' + str(test_case) + ' ' + str(cnt))