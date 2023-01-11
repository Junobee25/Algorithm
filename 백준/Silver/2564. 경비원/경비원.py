def location(num):
    if num == 1:  # 북쪽 이미 Y좌표 = M 고정값
        base[0][0] += cnt  # X값만 증가
        return base[0]
    elif num == 2:  # 남쪽 Y좌표 = 0 고정값
        base[1][0] += cnt  # X값만 증가
        return base[1]
    elif num == 3:  # 서쪽 X좌표 = 0 고정값
        base[2][1] += M-cnt  # Y값은 위쪽에서의 거리
        return base[2]
    elif num == 4:  # 동쪽 X좌표 = N 고정값
        base[3][1] += M-cnt  # Y값은 위쪽에서의 거리  
        return base[3]  


N,M = map(int,input().split())
K = int(input())

home = []  # 집의 좌표가 담긴 배열

length = 0  # 최소 거리들의 합
for i in range(K+1):  # i = 0, 1, 2, 3 ,,,,,, K
    base = [[0,M],[0,0],[0,0],[N,0]]  # 북 좌표,남 좌표,서 좌표, 동 좌표 초기화
    num,cnt = map(int,input().split())
    home.append(location(num))
    if i == K:  # 동근이가 집위치를 선택할때
        for j in range(K):
            if (home[j][1]==home[-1][1] and abs(home[j][0] - home[-1][0]) == N) or (home[j][0] == home[-1][0] and abs(home[j][1] - home[-1][1]) == M):  
                if sum(home[j]+home[-1]) <= (N+M)*2-sum(home[j]+home[-1]):
                    length += sum(home[j]+home[-1])
                else:
                    length += (N+M)*2 - sum(home[j]+home[-1])
            elif (home[j][0] ==0) and (home[-1][0]==0):  # 회사와 동근이 집이 같은 선상에 있을 경우
                length += [abs(ai-bi) for ai,bi in zip(home[j],home[-1])][1]
            elif (home[j][0] ==N) and (home[-1][0]==N):
                length += [abs(ai-bi) for ai,bi in zip(home[j],home[-1])][1]
            elif (home[j][1] ==0) and (home[-1][1]==0):
                length += [abs(ai-bi) for ai,bi in zip(home[j],home[-1])][0]
            elif (home[j][1] ==M) and (home[-1][1]==M):
                length += [abs(ai-bi) for ai,bi in zip(home[j],home[-1])][0]
            elif 0<home[j][0]<N and home[j][1] == 0 and home[-1][0] == N:
                length += abs(home[j][0]-home[-1][0]) +home[-1][1]
            elif 0<home[-1][0]<N and home[-1][1] == 0 and home[j][0] == N:
                length += abs(home[j][0]-home[-1][0]) +home[j][1]
            elif 0<home[j][1]<M and home[j][0] == 0 and home[-1][1] == M:
                length += abs(home[j][1]-home[-1][1]) +home[-1][0]
            elif 0<home[-1][1]<M and home[-1][0] == 0 and home[j][1] == M:
                length += abs(home[j][1]-home[-1][1]) +home[j][0]
            elif sum(home[j]+home[-1]) <= (N+M)*2-sum(home[j]+home[-1]):
                length += sum(home[j]+home[-1])
            else:
                length += (N+M)*2 - sum(home[j]+home[-1])
print(length)
