# while True:
#     decimal = int(input())
#     cnt = 0
#     if decimal == 0:
#         break
#     elif decimal == 1:
#         print(1)
#     elif decimal == 2:
#         print(2)
#     else:
#         for i in range(decimal,decimal*2+1):
#             cnt += 1
#             for j in range(2,i):
#                 if i%j == 0:
#                     cnt -=1
#                     break
#         print(cnt)
import math
def isPrime(x):
    if x == 1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True
while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for i in range(n+1,2*n+1):
        if isPrime(i):
            cnt += 1
    print(cnt)