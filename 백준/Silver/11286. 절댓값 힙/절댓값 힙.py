# 문제 이해
# 1) 배열에 원소를 삽입
# 2) 0이 입력되면 배열안에서 절댓값이 가장 작은 값을 출력 만약 가장 작은 값이 여러개라면 절댓 값을 하기전의 최솟값을 출력

# 접근
# 최소 힙에 (절대값,원래값) 삽입 최소힙에 절대값이 가장작고 원래값이 가장작은 루트노드가 생김
# 루트노드 출력 후 삭제
# 0 입력 시 힙이 비어있다면 0 출력

import heapq
import sys
input = sys.stdin.readline
n = int(input().rstrip())

q = []

for i in range(n):
    k = int(input().rstrip())
    if k != 0:
        heapq.heappush(q,(abs(k),k))
    elif k == 0:
        if len(q) == 0:
            print(0)
        else:
            min_data = heapq.heappop(q)
            print(min_data[1])
    
        
    