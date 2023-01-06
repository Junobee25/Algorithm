M,N = map(int,input().split())
arr = []
for i in range(M,N+1):
    if i > 1 :
        arr.append(i)
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                arr.pop()
                break

for i in arr:
    print(i)


