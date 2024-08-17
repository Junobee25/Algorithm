n, j, h = map(int, input().split())

def find_round(j, h):
    cnt = 0
    # 두 값이 같아질 때까지 계속 반복
    while j != h:
        j = (j + 1) // 2  # 다음 라운드로 이동
        h = (h + 1) // 2
        cnt += 1  # 라운드 증가
    return cnt

# 결과 출력
print(find_round(j, h))