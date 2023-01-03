T = int(input())
# 이차원 배열
for test_case in range(1, T + 1):
    arr = []  # 테스트 케이스 마다 배열 초기화
    result = 0  # 테스트 케이스 마다 수확량 초기화
    N = int(input())  # 농장 크기
    for i in range(N):
        arr.append(list(input()))  # 이차원 배열 생성
        for j in range(N):
            arr[i][j] = int(arr[i][j])  # 이차원 배열 요소 int형으로 초기화
        if (i > N//2):  # 중심 행보다 클때 감소하는 수확량에 대한 로직
            result += sum(arr[i][abs((N//2)-i): (N + (N-i) - N//2 - 1)])
        else:  # 중심 행까지 증가하는 수확량에 대한 로직
            result += sum(arr[i][abs((N//2)-i): (N//2 + 1 + i)])
    print("#" + str(test_case) + " " + str(result))
