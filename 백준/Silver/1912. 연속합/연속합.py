# 연속된 숫자의 합중 최대 값을 dp 테이블에 갱신 해야겠네?
# <이전 항까지의 합>과 현재 값 중에서 최대 값이 dp 테이블에 저장되는 형태로
N = int(input())
arr = list(map(int,input().split()))
for i in range(1,N):
    arr[i] = max(arr[i],arr[i-1]+arr[i])
print(max(arr))
