# 골드 바흐의 추측 (매우 어려웠다.)
# 생각 1. 소수 리스트를 만들어야겠다
# 생각 2. 소수 리스트에서 반복문을 돌리며 합을 찾아야겠다.
# 생각 3. 두수의 차이가 최소인 건 어떻게 찾지?
import sys
input = sys.stdin.readline
# 에라토스테네스의 체
arr = [True for _ in range(1000001)]

for i in range(2,1001):
    if arr[i] == True:
        for j in range(i+i,1000001,i):
            arr[j] = False

while True:
    N = int(input().rstrip())
    if N == 0 :
        break
    for i in range(3,1000001):
        if arr[i] and arr[N-i]:
            print(N,"=",i,"+",N-i)
            break