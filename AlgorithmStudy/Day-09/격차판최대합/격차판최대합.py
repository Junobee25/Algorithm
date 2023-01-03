import sys
input = sys.stdin.readline
N = int(input())
arr = []
# 이차원 배열
for i in range(N):
    arr.append(list(map(int,input().split())))

row_sum = 0  # 행들의 합 
col_sum = 0  # 열들의 합 
dia_sum = 0  # 대각선 합
for i in range(N):
    if row_sum < sum(arr[i]):  # 행들의 합들 중 최대 초기화 로직
        row_sum = sum(arr[i])
    columns = 0
    for j in range(N):  # 열요소는 행이 전부 돌고 바뀌기에 안쪽 포문의 매개변수 값을 i로 
        columns += arr[j][i]  # 열 요소의 합
    if col_sum < columns :  # 열들의 합들 중 최대 초기화 로직
        col_sum = columns
    dia_sum += arr[i][i]  # 대각선은 하나

print(max(row_sum,col_sum,dia_sum))