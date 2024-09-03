n = int(input())

arr = list(map(int,input().split()))

def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a

t = arr[0]

for i in range(1, len(arr)):
    k = gcd(t, arr[i])
    print(str(t//k) + "/" + str(arr[i]//k))