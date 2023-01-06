A,B,C = map(int,input().split())

k = (C-B)/(A-B)

if k == int(k):
    print(int(k))
else:
    print(int(k)+1)