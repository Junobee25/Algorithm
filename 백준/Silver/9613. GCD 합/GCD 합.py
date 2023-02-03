T = int(input())
def gcd(A,B):
    while A%B != 0:
        tmp = A%B
        A = B
        B = tmp
    return B
for i in range(T):
    result = 0
    arr = list(map(int,input().split()))
    for i in range(1,len(arr)):
        for j in range(i+1,len(arr)):
                result += gcd(arr[i],arr[j])
                
    print(result)
                  