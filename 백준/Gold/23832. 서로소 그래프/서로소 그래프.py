import math

def euler_totient(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1: 
        result -= result // n
    return result

n = int(input()) 

total = 0
for i in range(2, n + 1):
    total += euler_totient(i)

print(total)
