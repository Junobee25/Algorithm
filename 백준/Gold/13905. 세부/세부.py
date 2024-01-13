import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
home_cnt, bridge_cnt = map(int, input().split())
sung, hyebin = map(int, input().split())

parent = list(range(home_cnt + 1))
edges = []

for _ in range(bridge_cnt):
    home1, home2, cost = map(int, input().split())
    edges.append((cost, home1, home2))

edges.sort(reverse=True)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_find(parent, a, b):
    parent_of_a = find_parent(parent,a)
    parent_of_b = find_parent(parent,b)
    
    if parent_of_a < parent_of_b:
        parent[parent_of_b] = parent_of_a
    else:
        parent[parent_of_a] = parent_of_b
        
        
result = 0
for edge in edges:
    cost, home1, home2 = edge
    if find_parent(parent, home1) != find_parent(parent,home2):
        union_find(parent, home1, home2)
        
    if find_parent(parent, sung) == find_parent(parent, hyebin):
        result = cost
        break
        
print(result)      