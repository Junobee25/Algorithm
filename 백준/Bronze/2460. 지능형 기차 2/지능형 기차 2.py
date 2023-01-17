arr = []
c = 0
for i in range(10):
    a,b = map(int,input().split())
    c += b-a
    arr.append(c)

    

print(max(arr))