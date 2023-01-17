# N의 약수들 중 K번째로 작은 수
N,K = map(int,input().split())
result = []
for i in range(1,N+1):
    if N%i == 0:
        result.append(i)


if len(result) <K:
    print(0)
else:
    print(result[K-1])