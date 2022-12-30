N = 10
for i in range(1, N + 1): ## 10번의 Test Case해줄 for문
    M = int(input())  ## Dump 횟수
    arr = list(map(int, input().split())) ## 요소 100개짜리 리스트 갱신
    for j in range(M): ## Dump 횟수만큼 반복
        maxVal = max(arr) 
        minVal = min(arr)
        minIdx = arr.index(minVal) # 최댓값 초기화 하면서 인덱스까지 가져온다.
        maxIdx = arr.index(maxVal)
        arr[minIdx] += 1 # 최소는 +1
        arr[maxIdx] -= 1 # 최대는 -1
    answer = max(arr) - min(arr) # 평탄화 후 높낮이 차이 계산
    print("#", i, " ", answer, sep='')