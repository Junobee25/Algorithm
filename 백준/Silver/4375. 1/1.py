import sys

input = sys.stdin.readline

while True:
    try:
        n=int(input())
    except:
        break
    
    k = 1
    m = 1
    
    while True:
        if k % n == 0:
            print(len(str(k + m)))
            break
        else:
            m *= 10
            k = k + m