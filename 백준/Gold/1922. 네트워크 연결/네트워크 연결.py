n = int(input())
m = int(input())


def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_find(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

edges = []
parent = [0]*(n+1)

# 부모노드 자기자신
for i in range(1,n+1):
    parent[i] = i

# 노드,간선 정보와 비용
for _ in range(m):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()
result = 0
for edge in edges:
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_find(parent,a,b)
        result += cost

print(result)