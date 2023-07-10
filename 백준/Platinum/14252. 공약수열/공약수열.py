n = int(input())


arr = list(map(int,input().split()))

arr.sort()

def gcd(a,b):
    while b > 0:
        a,b = b, a%b
    return a

cnt = 0

if n == 1:
    print(0)
    exit()

else:
    for i in range(1,len(arr)):
        if gcd(arr[i-1],arr[i]) != 1:
            check = False
            for j in range(arr[i-1]+1,arr[i]):
                if gcd(arr[i],j) == 1 and gcd(arr[i-1],j) == 1:
                    check = True
            
            if check:
                cnt += 1

            else:
                cnt += 2
print(cnt)


            