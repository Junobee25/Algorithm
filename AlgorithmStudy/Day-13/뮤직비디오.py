import sys
input = sys.stdin.readline
def Count(capacity):  # 주어진 용량에 곡을 담은 후 DVD의 갯수
    cnt = 1
    sum = 0
    for x in Music:
        if sum+x>capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt

N,M = map(int,input().split())
Music = list(map(int,input().split())) 
lt = 1
rt = sum(Music)  # 용량의 크기를 이분탐색으로 줄여 나가기위한 rt 설정
res = 0  # 용량의 크기 초기화
maxx = max(Music)
while lt <= rt:
    mid = (lt+rt)//2
    if mid >= maxx and Count(mid)<=M:  # N
        res = mid  
        rt = mid -1
    else:
        lt = mid + 1

print(res)