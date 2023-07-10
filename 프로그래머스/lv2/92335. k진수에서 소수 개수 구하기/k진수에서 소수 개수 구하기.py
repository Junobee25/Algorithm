# 소수 판별 알고리즘
def isPrime(t):
    if(t<2):
        return False
    for i in range(2,int(t**(0.5))+1):
        if(t%i==0):
            return False
    return True


# 직접 진법 변환 후 문자열 나눠서 소수인지 판별해서 cnt 하기
def solution(n, k):
    change = ''
    cnt = 0

    while True:
        if n < k:
            change += str(n)
            break
        mod = n % k
        n = n//k
        change += str(mod)

    new_arr = change[::-1].split('0')
    for i in new_arr:
        if i == '':
            continue
        if(isPrime(int(i))):
            cnt += 1
    return cnt