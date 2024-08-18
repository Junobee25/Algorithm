import sys

input = sys.stdin.readline

n = int(input())

def is_prime(number):
    for i in range(2, int(number**(1/2)) + 1):
        if number % i == 0:
            return False
    return True



for i in range(n):
    k = int(input())
    while True:
        if k == 0 or k == 1:
            print(2)
            break
        if is_prime(k):
            print(k)
            break
        else:
            k += 1