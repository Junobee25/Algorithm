def makeTree(currentNode,parent):
    for node in graph[currentNode]:
        if node != parent:
            curNodeChildList[currentNode].append(node)
            makeTree(node,currentNode)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(150000)
# 직원수 n 칭찬 횟수 m
n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]

score_list = [0] * (n+1)

curNodeChildList = [[] for _ in range(n+1)]

relation = list(map(int,input().split()))

# 연결리스트 표현
for i in range(1,len(relation)):
    graph[i+1].append(relation[i])
    graph[relation[i]].append(i+1)

# 자식노드 그래프 만들기
makeTree(1,1)

# [[], [2, 3, 5], [4, 6], [7, 8], [], [9, 10], [], [], [], [], []]

def dfs(node):
    for n in curNodeChildList[node]:
        score_list[n] += score_list[node] 
        dfs(n)


for _ in range(m):
    curNode, score = map(int,input().split())
    score_list[curNode] += score

dfs(1)


for i in range(1,len(score_list)):
    print(score_list[i], end = " ")