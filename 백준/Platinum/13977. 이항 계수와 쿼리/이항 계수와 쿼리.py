import sys
input = sys.stdin.readline

m = int(input())

modular = 1000000007

def power(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    
    half = power(a, b//2)
    
    if b % 2:
        return half ** 2 * a % modular
    else:
        return half ** 2 % modular

factorial = [1]
for i in range(1, 4000001):
    factorial.append(factorial[i-1] * i % modular)
    
for _ in range(m):
    n, k = map(int, input().split())
    
    top = factorial[n]
    bot = factorial[n - k] * factorial[k] % modular
    
    print(top * power(bot, modular - 2) % modular)