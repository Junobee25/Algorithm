N,K = map(int,input().split())

coin_type = []

for i in range(N):
    coin = int(input())
    coin_type.append(coin)

result = K
cnt = 0
i = N-1
while result > 0:
    if result - coin_type[i] < 0:
        i -= 1
        pass
    elif result - coin_type[i] >= 0 :
        result = result - coin_type[i]
        cnt+=1
print(cnt)