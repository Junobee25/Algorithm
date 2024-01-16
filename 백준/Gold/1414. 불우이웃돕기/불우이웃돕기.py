N = int(input())

lan_cable_info = []
for _ in range(N):
    lan_cable_info.append(list(input()))

parent = list(range(N))
edges = []
total = 0

for i in range(N):
    for j in range(N):
        if lan_cable_info[i][j] == '0':
            edges.append((0,i,j))
        else:
            if lan_cable_info[i][j].islower():
                total += ord(lan_cable_info[i][j]) - ord('a') + 1
                edges.append((ord(lan_cable_info[i][j]) - ord('a') + 1, i, j))
            else:
                total += ord(lan_cable_info[i][j]) - ord('A') + 27
                edges.append((ord(lan_cable_info[i][j]) - ord('A') + 27, i, j))
                
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] =  find_parent(parent, parent[x])
    return parent[x]

def union_find(parent, a, b):
    parent_of_a = find_parent(parent, a)
    parent_of_b = find_parent(parent, b)
    
    if parent_of_a < parent_of_b:
        parent[parent_of_b] = parent_of_a 
    else:
        parent[parent_of_a] = parent_of_b
        
result = 0


edges.sort()

for edge in edges:
    cost, computer1, computer2 = edge
    
    if cost == 0:
        continue
    
    if find_parent(parent, computer1) != find_parent(parent, computer2):
        union_find(parent, computer1, computer2)
        total -= cost
        
node = set()    
for i in range(N):
    if find_parent(parent,i) not in node:
        node.add(find_parent(parent,i))

if len(node) == 1:
    print(total)
else:
    print(-1)