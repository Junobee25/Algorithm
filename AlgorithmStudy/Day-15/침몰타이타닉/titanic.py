from collections import deque
N,M = map(int,input().split())
weight = list(map(int,input().split()))
weight.sort() 
weight = deque(weight)  # pop(0) 보다 popleft() 하는 것이 메모리적으로 효율적
cnt = 0
while weight:  # weight비교 후 전부 pop되면 while문 끝
    if len(weight) == 1:  # 1이면 weight[0] + weight[-1] 로직 x . popleft(),pop() 로직 x
        cnt += 1
        break
    if weight[0] + weight[-1] > M:
        weight.pop()
        cnt += 1
    else:
        weight.popleft()
        weight.pop()
        cnt += 1
print(cnt)