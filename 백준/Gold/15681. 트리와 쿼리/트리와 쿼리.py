import sys
input = sys.stdin.readline
sys.setrecursionlimit(150000)
n, r, q = map(int,input().split())

graph = [[] for _ in range(n+1)]

# graph에서 각 정점에 대한 자식노드의 관계 그래프
currentNodeChildList = [[] for _ in range(n+1)]

# subTreeList[u] => u번을 정점으로 하는 서브트리의 정점의 개수
subTreeList = [0]*(n+1)

def makeTree(currentNode,parent):
    for node in graph[currentNode]:
        if node != parent:
            currentNodeChildList[currentNode].append(node)
            makeTree(node,currentNode)

def countSubtreeNode(currentNode):
    subTreeList[currentNode] = 1
    for node in currentNodeChildList[currentNode]:
        countSubtreeNode(node)
        subTreeList[currentNode] += subTreeList[node]
            
# 가중치가 없는 무향그래프의 연결관계 인접리스트로 표현
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

makeTree(r,r)

resultNode = []
countSubtreeNode(r)
for _ in range(q):
    u = int(input())
    resultNode.append(u)

for n in resultNode:
    print(subTreeList[n])