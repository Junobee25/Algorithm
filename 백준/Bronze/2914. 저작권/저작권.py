A, I  = map(int,input().split())

k = A * I
t = I - 1

while True:
    q = k / A
    if q <= t:
        k += 1
        break
    k -= 1
print(k) 