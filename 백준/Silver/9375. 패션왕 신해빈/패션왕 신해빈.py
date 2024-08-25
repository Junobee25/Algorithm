import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    cloth = {}
    result = 1
    n = int(input())
    for _ in range(n):
        k, q = input().split()
    
        if q in cloth:
            cloth[q] += 1
        else:
            cloth[q] = 1
        
        

    for i in cloth.keys():
        result *= (cloth[i] + 1)
    print(result - 1)