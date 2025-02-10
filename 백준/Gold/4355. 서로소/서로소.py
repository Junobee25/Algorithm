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
while True:
    n = int(input()) 
    if n == 0:
        break
    elif n == 1:
        print(0)
    else:
        print(euler_totient(n))


