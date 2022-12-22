N, M = map(int,input().split())

# N, M면체 주사위 눈 리스트로 반환
N_poly = [i+1 for i in range(N)]
M_poly = [i+1 for i in range(M)]

# 두 주사위 눈의 합을 담을 리스트 생성
PlusNM = []

# 최대값 구하기 위해 NMmax 설정
NMmax = -999999

# count함수와 사용과 오름차순으로 정렬하기 위해 답 리스트 생성
solution = []

# 두 주사위의 눈의 합 PlusNM에 추가 (중복 값)
for i in N_poly:
    for j in M_poly:
        PlusNM.append(i+j)

# 중복된 값의 개수가 최대인 지점 찾기 (최대 => 확률 가장 높음)
for i in PlusNM:
    if NMmax < PlusNM.count(i):
        NMmax = PlusNM.count(i)

# 최대인 지점이면 답 리스트에 추가
for i in PlusNM:
    if PlusNM.count(i) == NMmax:
        solution.append(i)

# set을 통해 중복제거 후 오름차순 해결
for i in set(solution):
    print(i,end=" ")
    







