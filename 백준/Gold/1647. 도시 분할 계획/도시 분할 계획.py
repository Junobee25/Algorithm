n,m = map(int,input().split())

parent = [0]*(n+1)


edges = []
result = 0
for i in range(1, n + 1):
    parent[i] = i
for _ in range(m):
    n,m,c = map(int,input().split())
    edges.append((c,n,m))
# 최소신장트리를 만들기 위해 cost기준으로 오름차순 정렬 => 비용이 적을 값들 먼저 그리디 하게 간선으로 연결
edges.sort()
# 재귀호출을 통해 노드의 부모노드를 찾음
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

max_val = 0
# 부모노드가 같은 값들을 같은 그룹으로 묶기
def union_find(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
for edge in edges:
    cost,a,b = edge # edge에서 하나씩 꺼내서 union find하기
    if find_parent(parent,a) != find_parent(parent,b):
        union_find(parent,a,b)
        result += cost
        max_val = cost
# 최소신장트리로 만들어진 노드에서 최댓값을 찾아야함
# print(result-edges[-1][0])
print(result-max_val)
    