T = int(input())
finish = 0
for i in range(T):
    k = int(input())
    n = int(input())
    a = 1
    b = 1
    for i in range(k+1):
        a *= n+i
        b *= i+1
    c = round(a/b)
    print(c)
    