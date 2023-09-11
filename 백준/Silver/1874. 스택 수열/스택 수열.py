import sys
input = sys.stdin.readline

n = int(input())

stack = []
arr = []
result = ''
for _ in range(n):
    arr.append(int(input()))

cnt = 0


end = 0
flag = True
for i in range(n):
    if arr[i] > end:
        for j in range(end + 1, arr[i] + 1):
            stack.append(j)
            result += '+'
        stack.pop()
        result += '-'
        end = arr[i]
    elif end > arr[i]:
        if stack[-1] == arr[i]:
            stack.pop()
            result += '-'
        else:
            flag = False
            print("NO")
            break

if flag:
    for i in result:
        print(i)