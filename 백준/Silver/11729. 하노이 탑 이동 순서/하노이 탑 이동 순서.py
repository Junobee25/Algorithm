
cnt = 0
def hanoi(n,start,end,mid):
    global cnt
    if n == 1:
        print(start,end) 
        return
    else:
        hanoi(n-1,start,mid,end)
        print(start,end)
        hanoi(n-1,mid,end,start)
n = int(input())
print(2**n-1)
hanoi(n,1,3,2)