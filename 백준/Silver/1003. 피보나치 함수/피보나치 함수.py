T = int(input())

for _ in range(T):
    zero, one = 1, 0
    N = int(input())
    for i in range(N):
        zero,one = one, zero+one
    print(zero,one)
    