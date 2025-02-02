import sys
import math
input = sys.stdin.readline

a = int(input())
b = int(input())
check = [2, 3, 5, 7, 11, 13, 17]

pera = a / 100.0
perb = b / 100.0
sa = sb = 0

for prime in check:
    combi = math.comb(18, prime)
    sa += combi * pow(pera, prime) * pow(1.0 - pera, 18 - prime)
    sb += combi * pow(perb, prime) * pow(1.0 - perb, 18 - prime)

print(sa + sb - sa * sb)