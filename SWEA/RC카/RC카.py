# import sys
# input = sys.stdin.readline
# T = int(input())

# for test_case in range(1, T + 1): 
#     N = int(input())
#     result = 0  # 총 간 거리
#     my_speed = 0  # 증감 할 속도
#     for i in range(N):
#         case,speed = map(int,input().split())
#         if case == 1 :  # 속도 증가
#             my_speed += speed
#             result += my_speed
#         elif case == 0 :  # 속도 유지
#             result += my_speed
#         elif case == 2:  # 속도 감소
#             if my_speed < speed:  # 현재 속도보다 감속할 속도가 더 클 경우, 속도 0 로직
#                 result += my_speed
#             else:
#                 my_speed -= speed
#                 result += my_speed
#     print("#", test_case, " ", result, sep="")


# 입력 값 0에대해서 int형으로 처리 받을 방법이 없어서 리스트를 이용해서 풀었습니다.

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    result = 0  # 총 간 거리
    my_speed = 0  # 증감 할 속도
    for i in range(N):
        arr = list(map(int,input().split()))

        if arr[0] == 0 :  # 속도 유지
            result += my_speed
        if arr[0] == 1 :  # 속도 증가
            my_speed += arr[1]
            result += my_speed
        if arr[0] == 2 :  # 속도 감소
            if my_speed < arr[1] :  # 현재 속도보다 감속할 속도가 더 클 경우, 속도 0 로직
                result += my_speed
            else :
                my_speed -= arr[1]
                result += my_speed
    print("#" + str(test_case) + " " + str(result), sep="")