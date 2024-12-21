n = int(input())

a = 0
b = 0
for _ in range(n):
    k = int(input())

    if k:
        a += 1
    else:
        b += 1

if a > b:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")