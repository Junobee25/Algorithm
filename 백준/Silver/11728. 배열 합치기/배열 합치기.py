# 배열 A의 크기 배열 B의 크기
N,M = map(int,input().split())

# 두 배열을 합친 후 정렬한 결과

A = list(map(int,input().split()))
B = list(map(int,input().split()))

arr = A + B
arr.sort()

for i in arr:
    print(i, end = " ")
