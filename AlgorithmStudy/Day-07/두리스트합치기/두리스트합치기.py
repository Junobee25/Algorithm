import sys
input = sys.stdin.readline
N = int(input())
# 리스트 만들기
N_list=list(map(int,input().split()))
M = int(input())
# 리스트 만들기
M_list=list(map(int,input().split()))
# 오름차순 정렬
new_list = sorted((N_list) + (M_list))

print(new_list)