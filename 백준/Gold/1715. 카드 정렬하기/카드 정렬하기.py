# 문제 이해
# 카드 묶음을 두 묶음씩 서로 합쳐 나갔을 때
# 비교 횟수의 최소값

# 접근
# 완전 이진트리 힙 자료구조를 만들어서
# 부모노드와 자식노드 1개를 빼서 더해보자
# 그리고 그 합을 변수에 저장하고
# 그 합을 이진트리에 push한다.
# 이 과정을 반복


import heapq
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = []
for i in range(n):
    arr.append(int(input().rstrip()))
heapq.heapify(arr)
result = 0
if n == 1:
    print(result)
else:
    for i in range(n-1):
        pre = heapq.heappop(arr)
        con = heapq.heappop(arr)

        result += pre + con
        heapq.heappush(arr,pre + con)
    print(result)