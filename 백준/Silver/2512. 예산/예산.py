# 문제 이해
# 정해진 예산에서 모든 국가에데 가능한 한 최대의 총 예산을 나눠주기
# 모든요청 가능 => 그대로
# 모든요청 불가능 => 상한액 정하기 (상한액 보다 작으면 그대로/ 크면 상한액으로 주기)

# 접근
# target = M
# 예산배정(상한) < M  => 늘리기
# 예산배정(상한) >= M => 줄이기

n = int(input())
request_budget = list(map(int,input().split()))
total_budget = int(input()) # target값

# 이분탐색을 위한 정렬
request_budget.sort()

left = 0
right = max(request_budget)


target = 0
while left<=right:
    max_budget = 0
    mid = (left + right)//2
    for i in request_budget:
        if i > mid:
            max_budget += mid
        else:
            max_budget += i

    if max_budget > total_budget:
        right = mid - 1
    else:
        left = mid + 1
        target = mid
print(target)


    


