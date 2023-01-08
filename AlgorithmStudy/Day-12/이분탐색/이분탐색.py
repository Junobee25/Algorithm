N,M = map(int,input().split())
number = list(map(int,input()))

min_num = 999999

number.sort()  # 이분탐색 => 중간값이 찾고자 하는 값보다 클때와 작을때를 기준으로 범위를 좁혀 나가는 탐색

lt = 0  # 왼쪽 끝
rt = N-1  # 오른쪽 끝

while lt <= rt:  # rt를 기준으로 중간위치의 값을 찾음
    mid = (lt+rt)//2  # 중간위치 값
    if number[mid] == M:
        print(mid+1)
        break
    elif number[mid] > M:
        rt = mid-1

    else:
        lt = mid + 1