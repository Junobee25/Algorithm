n,m = map(int,input().split())
arr = list(map(int,input().split()))
def one_change(p,c):
    arr[p-1] = c

def range_change(x1,x2):
    for i in range(x1-1,x2):
        if arr[i] == 0:
            arr[i] = 1
        else:
            arr[i] = 0
    
def off(x1,x2):
    for i in range(x1-1,x2):
        arr[i] = 0

def on(x1,x2):
    for i in range(x1-1,x2):
        arr[i] = 1


for t in range(m):
    a,b,c = map(int,input().split())
    if a == 1:
        one_change(b,c)
    elif a == 2:
        range_change(b,c)
    elif a == 3:
        off(b,c)
    else:
        on(b,c)
for k in arr:
    print(k, end = " ")
    