n, k = map(int, input().split())
m = 1000000007

def fac(a):
    t = 1
    for i in range(2, a + 1):
        t = (t * i) % m
    return t


def square(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    
    tmp = square(a, b//2)
    
    if b % 2:
        return tmp * tmp * a % m
    
    else:
        return tmp * tmp % m
    
top = fac(n)
bottom = fac(n -k) * fac(k) % m


print(top*square(bottom, m-2)%m)