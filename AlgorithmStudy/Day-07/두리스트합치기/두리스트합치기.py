# # SOL - 탐색&시뮬레이션
# import sys
# input = sys.stdin.readline
# N = int(input())
# # 리스트 만들기
# N_list=list(map(int,input().split()))
# M = int(input())
# # 리스트 만들기
# M_list=list(map(int,input().split()))
# # 오름차순 정렬
# new_list = sorted((N_list) + (M_list))

# print(new_list)
# --> 시간복잡도 NlogN
# # 포인터 개념

import sys
input = sys.stdin.readline
N = int(input())
# 리스트 만들기
N_list=list(map(int,input().split()))
M = int(input())
# 리스트 만들기
M_list=list(map(int,input().split()))
NM_list = []
# N 포인터
N_cnt = 0
# M 포인터
M_cnt = 0
# 둘중 하나 포인터 끝나는 cnt 세기
cnt = 0

# N,M중에 길이가 짧은 리스트를 기준으로 길이 만큼 반복
while cnt < min(N,M) :
    if N_list[N_cnt] >= M_list[M_cnt] :
        NM_list.append(M_list[M_cnt])
        M_cnt += 1
    else:
        NM_list.append(N_list[N_cnt])
        N_cnt += 1
    cnt += 1
    
# 슬라이싱으로 남는 부분 붙이기
if len(N_list) >= len(M_list) :
    for i in (NM_list + N_list[M_cnt:]) :
        print(i, end = " ")
    
else:
    for i in (NM_list + M_list[N_cnt:]):
        print(i, end = " ")

# 시간복잡도 N
# NlogN -> N