n = int(input())

arr = []

cnt = 1



for i in range(n):
    arr.append(list(map(int,input().split())))

arr.sort(key = lambda x : (x[1],x[0]))

end_time = arr[0][1]


for i in range(1,n):
    if end_time <= arr[i][0]:
        cnt += 1
        end_time = arr[i][1]
        
print(cnt)

