import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    consistency = "YES"
    phone_book = []
    
    N = int(input())
    for _ in range(N):
        phone_book.append(input().rstrip())
    phone_book.sort(key = lambda x : x[0:])
    
    for i in range(1, N):
        if phone_book[i].startswith(phone_book[i - 1]):
            consistency = "NO"
            break
    print(consistency)