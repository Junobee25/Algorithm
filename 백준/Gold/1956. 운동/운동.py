v, e = map(int, input().split())

INF = 10**9
graph = [[INF] * (v + 1) for _ in range(v + 1)]

for v1 in range(1, v + 1):
    for v2 in range(1, v + 1):
        if v1 == v2:
            graph[v1][v2] = 0
            
for _ in range(e):
    v1, v2, cost = map(int, input().split())
    graph[v1][v2] = cost
    
    
for k in range(1, v + 1):
    for v1 in range(1, v + 1):
        for v2 in range(1, v + 1):
            graph[v1][v2] = min(graph[v1][v2], graph[v1][k] + graph[k][v2])
            
max_distance = INF

for i in range(1, v + 1):
    for j in range(i, v + 1):
        if i != j:
            if graph[i][j] + graph[j][i] < max_distance:
                max_distance =  graph[i][j] + graph[j][i]
                
print(max_distance if max_distance != INF else -1)