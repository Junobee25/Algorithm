N = int(input())
a,b = 1,1
for i in range(2,N):
    a,b = a+b,a
if N == 1:
    print(1)
elif N==2:
    print(1)
else:
    print(a)
