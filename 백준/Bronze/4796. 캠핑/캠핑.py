# 문제 이해
# 주어진 휴가 동안에 최대한 캠핑장을 많이 이용하고 싶다.!
# 연속하는 y일 동안 x일만 이용할 수 있다!

circle = 0
while True:
    l,p,v = map(int,input().split())
    if l == 0 and p == 0 and v == 0:
        break 
    cnt = 0
    while v >= p:
        cnt += 1
        v -= p
    circle += 1
    if v <= l :
        print(f"Case {circle}:",(l*cnt) + v)
    else:
        print(f"Case {circle}:",(l*cnt) + l)