import math

N, K, M = map(int, input().split())

list_n = []
list_k = []
s = 1

while N != 0:
    list_n.append(N%M)
    list_k.append(K%M)
    N//=M
    K//=M

for i in range(len(list_n)):
    s *= math.comb(list_n[i], list_k[i])
    
print(s%M)