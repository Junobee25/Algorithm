import sys
input = sys.stdin.readline
N, M = map(int,input().split())
arr = list(map(int,input().split()))

start = 0 # 시작 인덱스
end = 0 # 끝 인덱스
cnt = 0 # 경우의 수 카운트
while True:
    if sum(arr[start:end+1]) == M : # arr[0:1]부터 시작해서 요소 합이 3이면 경우의수 , 인덱스 증가
        cnt += 1
        start += 1
        end += 1
    if end == N: 
        break 
    if sum(arr[start:end+1]) < M : # 시작인덱스는 그대로 두고 끝 부분인덱스를 늘려 합이 증가하면서 3에 근접하도록
        end += 1
    if sum(arr[start:end+1]) > M : # 끝 인덱스는 그대로 두고 시작인덱스를 늘려 합이 감소하면서 3에 근접하도록
        start += 1
print(cnt)