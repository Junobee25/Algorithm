n , k = list(map(int,input().split()))

Divisor_List = []

for i in range(n):
    if n % (i+1) == 0 :
        Divisor_List.append(i+1)

if k >= len(Divisor_List) :
    print(-1)
else :
    print(Divisor_List[k-1])


