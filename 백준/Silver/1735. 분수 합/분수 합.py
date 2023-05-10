a,b = map(int,input().split())
c,d = map(int,input().split())

up = 0
down = 0




def gcd(a,b):
    while a % b > 0:
        a,b = b, a%b
    return b

g = gcd(a*d+b*c, b*d)
print((a*d+b*c)//g,(b*d)//g)