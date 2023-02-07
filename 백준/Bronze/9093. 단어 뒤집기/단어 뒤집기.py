# 문자열을 검색하면서 띄어쓰기 말날때마다
# 역순으로 문자열 뒤집기 다시 띄어쓰기 만날때까지
T = int(input())

for i in range(T):
    arr = input()
    arr+=' '
    stack = []
    for j in range(len(arr)):
        if arr[j] != ' ':
            stack.append(arr[j])
        else:
            while stack:
                k  = stack.pop()
                print(k,end="")
            print(' ',end="")
                
