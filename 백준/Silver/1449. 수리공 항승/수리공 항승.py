# 문제 이해
# 물을 막을 때 적어도 그 위치의 좌우 0.5만큼 간격을 줘야 물이 다시는 안 샌다.
# 길이가 L인 테이프가 무한대로 주어짐

# 접근
# 데이터 정렬
# 최솟값의 -0.5를 뺀 값에서 부터 L을 더해줌 cnt += 1
# 리스트 선형탐색 중 다음 요소가 (a - 0.5 + L) 보다 작다면 pass
# 만약에 크다면 그 요소를 기준으로 (a2 - 0.5 + L) cnt += 1

n, l = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
tape = arr[0] - 0.5 + l
cnt = 1
for i in range(1,len(arr)):
    if tape > arr[i]:
        pass
    elif tape < arr[i]:
        tape = arr[i] - 0.5 + l
        cnt += 1
print(cnt)