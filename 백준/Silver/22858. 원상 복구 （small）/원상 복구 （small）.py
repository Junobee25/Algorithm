from copy import deepcopy
n, k = map(int,input().split())

S = list(map(int,input().split()))
D = list(map(int,input().split()))


change_dix = {}

# 역방향으로 추적해야되니
# key -> value로 추적

for i in range(len(D)):
    if D[i]-1 not in change_dix.values():
        change_dix[i] = D[i] - 1


for i in range(k):
    S_T = deepcopy(S)
    for k,v in change_dix.items():
        S [v] = S_T[k]

for i in S:
    print(i, end = " ")