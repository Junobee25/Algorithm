from collections import deque
# 테스트 케이스
T = int(input())
# 문서의 갯수 # 출력하고자하는 문서의 현재 위치
for i in range(T):
    N,M = map(int,input().split())

    # 차례대로 주어진 문서의 중요도
    important = [(pos,val) for pos,val in enumerate(list(map(int,input().split())))]
    important = deque(important)
    # 중요도에 따라서 출력
    cnt = 0
    # 뽑자가 하는 문서가 몇번째로 출력되는지
    while True:
        cur = important.popleft()
        if any(cur[1]<x[1] for x in important):
            important.append(cur)
        else:
            cnt += 1
            if cur[0] == M:
                break
    print(cnt)