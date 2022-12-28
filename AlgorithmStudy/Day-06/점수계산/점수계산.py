import sys
input = sys.stdin.readline

N = int(input())
CaseResult = list(map(int,input().split()))
score = 0
cnt = 0

# 가중치 개념 다시 복습하기
for i in CaseResult:
    if i == 1 :
        cnt += 1
        score += cnt
    else :
        cnt = 0
print(sum)