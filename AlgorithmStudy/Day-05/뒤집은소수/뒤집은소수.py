import sys
input = sys.stdin.readline

def reverse(x):
    res = 0
    while x > 0:
        # 일의자리 숫자 추출
        t = x%10
        # 일의 자리숫자부터 10씩 곱해주면서 숫자 갱신
        res = res*10+t
        # 갱신한 숫자 버리기 
        x = x//10
    return res

def isPrime(x):
    if x == 1:
        return False
    # 2부터 약수가 될 수있는 수까지 나뉘어 졌을때 False 반환
    for i in range(2,x//2):
        if x % i == 0:
            return False
    else:
        return True

N = int(input())
a = list(map(int, input().split()))

# 숫자 뒤집기 후 소수 판별 후 출력
for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp,end=' ')