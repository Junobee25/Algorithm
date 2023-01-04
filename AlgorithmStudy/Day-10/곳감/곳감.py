# import sys
# input = sys.stdin.readline

# N = int(input())
# arr = []

# # 이차원 배열로 마당 만들기
# for i in range(N):
#     arr.append(list(map(int,input().split())))
    
# print(arr)
# # 같은 배열을 생성해 인덱스를 회전시키려고 CompareArr = arr 해줬지만 CompareArr 또한 arr를 참조하여 해결하지 못함
# CompareArr = [[10,13,10,12,15],[12,39,30,23,11],[11,25,50,53,15],[11,25,50,53,15],[19,27,29,37,27],[19,13,30,13,19]]
# M = int(input())
# # 회전 로직
# for i in range(M):
#     ro = list(map(int,input().split()))  # ro = [행, 방향, 얼마나]
#     for j in range(N):
#         if ro[1] == 0 :  # 왼쪽                       ## 회전 로직 다시 생각해보기
#             arr[ro[0]-1][j] = CompareArr[ro[0]-1][j-ro[2]+1]
#         elif ro[1] == 1 :  # 오른쪽
#             arr[ro[0]-1][j] = CompareArr[ro[0]-1][j-ro[2]]
# print(arr)
# result = 0
# for i in range(N):
#     if i <= N//2:
#         result += sum(arr[i][i:N-i])
#     elif i > N//2:
#         result += sum(arr[i][N-i-1:i+1])
# print(result)

import sys
input = sys.stdin.readline
N = int(input())
# 이차원 배열 생성
arr = [list(map(int,input().split())) for _ in range(N)]
M = int(input())
for i in range(M):
    row, direction, move = map(int,input().split())
    if direction == 0:
        for _ in range(move):
            arr[row-1].append(arr[row-1].pop(0)) # pop으로 첫번째 요소를 빼고 append를 이용해 왼쪽으로 move큼 이동 
        else:
            for _ in range(move):
                arr[row-1].insert(0,arr[row-1].pop()) # pop으로 마지막 요소를 빼고 insert를 이용해 오른쪽으로 move만큼 이동