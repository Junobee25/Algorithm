import sys
input = sys.stdin.readline

s = input()
res = 0
cnt = 0
# isdecimal() -> 문자열에서 숫자일때 True를 반환 제곱도 포함
for i in s:
    if i.isdecimal() :
        # 0제외하고 숫자 만드는 알고리즘
        res = res*10 + int(i)
# 소수 찾기 알고리즘
for i in range(1,res+1):
    if res % i == 0 :
        cnt += 1

print(res)
print(cnt)
