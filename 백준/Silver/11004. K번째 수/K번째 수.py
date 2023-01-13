N,K = map(int,input().split())
result = list(map(int,input().split()))
result.sort()
print(result[K-1])