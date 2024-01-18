

N = int(input())
distance = list(map(int, input().split()))
oil_cost = list(map(int, input().split()))

currnet_oil_cost = oil_cost[0]
current_distance = 0
result = 0

for i in range(N - 1):
    if oil_cost[i] >= currnet_oil_cost:
        result += currnet_oil_cost * distance[i]
    else:
        currnet_oil_cost = oil_cost[i]
        result += currnet_oil_cost * distance[i]
print(result)