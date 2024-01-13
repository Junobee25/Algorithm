import sys
input = sys.stdin.readline
planet_cnt = int(input())

planet_connection = []
edges = []
parent = list(range(planet_cnt + 1))
result = 0

for _ in range(planet_cnt):
    connection = list(map(int, input().split()))
    planet_connection.append(connection)
    
    
for planet_1 in range(len(planet_connection) - 1):
    for planet_2 in range(planet_1, len(planet_connection)):
        if (planet_1 != planet_2):
            cost = planet_connection[planet_1][planet_2]
            edges.append((cost, planet_1, planet_2))

edges.sort()

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_find(parent, a, b):
    parent_of_a = find_parent(parent, a)
    parent_of_b = find_parent(parent, b)
    
    if parent_of_a < parent_of_b:
        parent[parent_of_b] = parent_of_a
    else:
        parent[parent_of_a] = parent_of_b
        
        
for edge in edges:
    cost, pla1, pla2 = edge
    if find_parent(parent, pla1) != find_parent(parent, pla2):
        union_find(parent, pla1, pla2)
        result += cost

print(result)