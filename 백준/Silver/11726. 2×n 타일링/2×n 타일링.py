N = int(input())
a,b = 3,2
for i in range(N-3):
    a,b = a+b,a
if N == 1:
    print(1%10007)
elif N==2:
    print(2%10007)
else:
    print(a%10007)


