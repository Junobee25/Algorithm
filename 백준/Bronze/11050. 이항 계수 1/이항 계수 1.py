N,k = map(int,input().split())

def Up(num):
    start = 1
    for i in range(k):
        start*=(num - i)
    return start

def Down(num):
    end = 1
    for i in range(k):
        end*=(num-i)
    return end
print(int(Up(N)/Down(k)))
