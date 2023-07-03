# N보다 크거나 같고 소수이면서 팰린드롬 수이면서 가장 작은 수
# 31 
n = 1000000
k = int(input())
arr = [False,False] + [True]*(n-1)

if k >= 98689:
    print(1003001)
    exit()
primes = []

for i in range(2,n+1):
    if arr[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            arr[j] = False

for i in range(len(primes)):
    primes[i] = str(primes[i])

new_primes = []

for i in range(len(primes)):
    if primes[i][::-1] == primes[i]:
        new_primes.append(int(primes[i]))

for i in new_primes:
    if i >= k:
        print(i)
        break