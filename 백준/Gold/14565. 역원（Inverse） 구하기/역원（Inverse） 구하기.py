def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

def xgcd(a,b):
    x = a
    y = b
    r1 = 1
    s1 = 0
    r2 = 0
    s2 = 1
    while True:
        q = x // y
        r = x % y
        r3 = r1 - r2*q
        s3 = s1 - s2*q

        if r == 0:
            return r2
        x = y
        y = r
        r1 = r2
        s1 = s2
        r2 = r3
        s2 = s3
    

n, a = map(int, input().split())

if gcd(a, n) !=1:
    inv = -1
else:
    inv = xgcd(a, n)
    while inv <= 0:
        inv += n

print(n - a, inv)