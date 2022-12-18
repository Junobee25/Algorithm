# 함수 만들기
# def add(a,b):
#     c = a + b
#     print(c)
# add(3,2)
# def add(a,b):
#     c = a + b
#     return c
# add(3,2) # print 해줘야 출력
# print(add(3,2))

# return 값 2개 튜플형으로 여러개의 값을 반환할 수 있다.
def add(a, b):
    c = a + b
    d = a - b
    return c, d


print(add(3, 2))

# 소수 판정 함수로 소수 구하기 알고르짐


def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False  # if False가 리턴 되면 함수가 종료 됨 
    return True


a = [12, 13, 7, 9, 19]

for y in a:
    if isPrime(y):
        print(y, end=' ')
