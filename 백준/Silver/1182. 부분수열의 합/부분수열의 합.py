# N개의 정수로 이루어진 수열이 있다
# 크기가 양수인 부분 수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는
# 경우의 수를 구하기
# 중복 조합..?

# 20C10 => 18만 정도이니 괜찮을듯
# 수열의 길이가 N까지이니
# 1~N까지의 상태공간을 만들고
# 상태공간크기만큼 나올 수있는 수열을 구한다음
# 합이 S이면 cnt += 1
from itertools import combinations

n,s = map(int,input().split())
arr = list(map(int,input().split()))

cnt = 0

for length in range(1,n+1):
    for com in combinations(arr,length):
        if sum(com) == s:
            cnt += 1
print(cnt)
