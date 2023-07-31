w,h = map(int,input().split())
x,y = map(int,input().split())
t = int(input())



cycle_x = 2 * w
cycle_y = 2 * h


if (cycle_x + t + x) % cycle_x > w:
    x = cycle_x - (cycle_x + t + x) % cycle_x
else:
    x = (cycle_x + t + x) % cycle_x


if (cycle_y + t + y) % cycle_y > h:
    y = cycle_y - (cycle_y + t + y) % cycle_y
else:
    y = (cycle_y + t + y) % cycle_y

print(x,y)

