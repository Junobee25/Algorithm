from math import log, pi

def logfact(x):
    return x*(log(x) - 1) + log(2*pi*x)/2 + 1/(12*x)

nf = int(input())

data = {1:1, 2:2, 6:3, 24:4, 120:5, 720:6, 5040:7, 40320:8, 362880:9, 3628800:10, 39916800:11, 479001600:12, 6227020800:13, 87178291200:14, 1307674368000:15, 20922789888000:16, 355687428096000:17, 6402373705728000:18, 121645100408832000:19}
if nf in data.keys(): print(data[nf]); quit()

start, end, mid = 20, 10**6, 500000
error = float(1e-3)

x = log(nf)

while True:
    mid  = (start + end) // 2
    if logfact(mid) > x + error:
        end = mid
    elif logfact(mid) < x - error:
        start = mid
    else:
        print(mid); quit()
