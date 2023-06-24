from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    cnt = 0
    compare_diff = 0
    if sum(q1) == sum(q2):
        return 0
    else:
        # q1이 더 크다고 가정
        if sum(q1) > sum(q2):
            compare_diff = sum(q1) - sum(q2)
            # while문안에서 sum으로 비교하는 것은 O(n^2) 시간 초과
            # compare_dff > 0 일때 compare_diff < 0 어디서 빼야할지 생각하기
            while compare_diff != 0 :
                # 일단 compare_diff 는 양수
                if cnt > (len(q1) + len(q2))*2:
                    cnt = -1
                    break
                if compare_diff > 0:
                    k = q1.popleft()
                    compare_diff -= k*2
                    q2.append(k)
                    cnt += 1
                elif compare_diff < 0:
                    k = q2.popleft()
                    compare_diff += k*2
                    q1.append(k)
                    cnt += 1 
        elif sum(q1) < sum(q2):
            compare_diff = sum(q2) - sum(q1)
            # while문안에서 sum으로 비교하는 것은 O(n^2) 시간 초과
            # compare_dff > 0 일때 compare_diff < 0 어디서 빼야할지 생각하기
            while compare_diff != 0 :
                # 일단 compare_diff 는 양수
                if cnt > (len(q1) + len(q2))*2:
                    cnt = -1
                    break
                if compare_diff > 0:
                    k = q2.popleft()
                    compare_diff -= k*2
                    q1.append(k)
                    cnt += 1
                elif compare_diff < 0:
                    k = q1.popleft()
                    compare_diff += k*2
                    q2.append(k)
                    cnt += 1
    return cnt