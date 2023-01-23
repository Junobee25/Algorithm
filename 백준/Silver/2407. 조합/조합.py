N,K= map(int,input().split())
p = [1]*(N+1)
for i in range(1,N):
    p[i] = p[i-1]*(N-i+1)//i
print(p[K])