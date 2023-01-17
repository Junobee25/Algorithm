# x -> y -> arr[y][x] 한수의 위치    (0,0) -> (w,y)
# 한수가 직사각형의 경계선 까지 가는 거리의 최솟값

# x,y,w,h
x,y,w,h = map(int,input().split())

if x != w or y != h or x != 0 or y != 0:
    print(min(y,x,h-y,w-x))
elif y == 0:
    print(min(y,h-y))
elif x == 0:
    print(min(x,w-x))
