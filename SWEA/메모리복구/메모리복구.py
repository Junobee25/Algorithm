T = int(input())

for test_case in range(1, T+1):
    cnt = 0
    arr = list(map(int,input()))
    i = 0
    while i < len(arr):
        if arr[i] == 1 :  # 처음 1일 나올 때 그 오른쪽 영역에서만 로직생각
            cnt += 1  # 1일 때는 0으로 바꿔줘야 하므로 count
            for j in range(i,len(arr)):  # 1다음의 숫자들을 바꿔주는 for문 
                if arr[j] == 1 :  # 1이면 0으로 하고 continue
                    arr[j] = 0
                    continue
                elif arr[j] == 0:  # 0이면 1으로함
                     arr[j] = 1
        i+=1  # 인덱스 증가 
    print('#' + str(test_case) + " " + str(cnt))