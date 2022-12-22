N = int(input())
score = list(map(int,input().split()))
avg_score = round(sum(score)/len(score))
score_min = float('inf')
min_list = []

# 평균점수와 학생점수 차이의 최솟값 구하기 
for i in range(len(score)):
    if abs(avg_score-score[i]) < score_min :
        score_min = abs(avg_score-score[i])

# 차이가 최솟값과 같다면 min_list에 학생점수 추가
for i in range(len(score)):
    if abs(avg_score-score[i]) == score_min :
        min_list.append(score[i])

# 평균점수, 평균과의 차이가 최솟값인 학생중에서 최대점수 출력
# index 함수 이용하여 중복시 제일 앞자리 숫자 출력
print(avg_score,score.index(max(min_list))+1,end=" ")