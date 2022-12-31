N = int(input())
for k in range(1, N + 1):
    arr = [list(map(int, input().split())) for _ in range(9)] # 이차원 배열 생성
    rowArr = arr # 행배열
    colArr = [[arr[i][j] for i in range(9)] for j in range(9)] # 열배열
    sqrArr = [[arr[i % 3 * 3 + j // 3][i // 3 * 3 + j % 3] for j in range(9)] for i in range(9)] # 3X3 배열
    answer = 1 
    for row, col, sqr in zip(rowArr, colArr, sqrArr):
        if len(set(row)) == len(set(col)) == len(set(sqr)) == 9: # set을 통해 집합길이가 9이면 continue
            continue
        else: 	# 9가 아닐시 중복이 있는 것이므로 0 반환
            answer = 0
            break
    print("#", k, " ", answer, sep="")