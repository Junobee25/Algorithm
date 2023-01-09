T = int(input())
arr = [[0 for i in range(100)] for i in range(100)] # 100x100

for i in range(T):
    start,end = map(int,input().split())
    for i in range(start,start+10):
        for j in range(end,end+10):
            arr[i][j] = '*'

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == '*':
            cnt +=1
print(cnt)