N = int(input())
def gcd(x,y):
        while y>0:
            x,y = y,x%y
        return x
for i in range(N):
    a,b = map(int,input().split())
    print(int((a*b)/gcd(b,a)))
  