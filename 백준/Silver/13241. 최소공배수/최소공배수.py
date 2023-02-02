A,B = map(int,input().split())
def gcd(A,B):
    while A%B !=0:
        tmp = A%B
        A = B
        B = tmp
    return B
print(A*B//gcd(A,B))