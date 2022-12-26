# 시간초과
# count = 0
# for i in range(N, 1, -1):
#     ad = 0
# i와 2~i-1까지의 숫자를 전부 비교하기 때문에 매우 비효율적인 연산
#     for j in range(2, i):       
#         if i % j == 0 :
#             ad += 1
#     if ad == 0:
#         count += 1
# print(count)
import sys
input = sys.stdin.readline
# 자연수의 개수 입력
N = int(input())
# 초기화할 배열 생성
prime_list = [0] * (N+1)
count = 0
for i in range(2,N+1):
    # 1.i가 소수라면 그 누구의 배수도 아니기 때문에 (1은제외) counting
    if prime_list[i] == 0:
        count +=1
        # 2. i(리스트의 인덱스)의 배수 위치의 값을 1로 초기화 하는 아이디어
        for j in range(i,N+1,i):
            prime_list[j] = 1
print(count)
# 설계순서 2 -> 1