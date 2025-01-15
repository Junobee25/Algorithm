ax,ay,bx,by = map(int,input().split())
cx,cy,dx,dy = map(int,input().split())
answer = 0
flag = False

def direct_vector(x1,y1,x2,y2):
    return (x2 - x1, y2 - y1)

def cross_product(vector_a, vector_b):
    return vector_a[0]* vector_b[1] - vector_a[1]*vector_b[0]


def CCW(x1,y1,x2,y2,x3,y3):
    a_vector = direct_vector(x1,y1,x2,y2)
    b_vector = direct_vector(x2,y2,x3,y3)

    k = cross_product(a_vector, b_vector)

    if k > 0:
        return 1
    elif k < 0:
        return -1
    else:
        return 0

if (CCW(ax,ay,bx,by,cx,cy) * CCW(ax,ay,bx,by,dx,dy) == 0 and CCW(cx,cy,dx,dy,ax,ay) * CCW(cx,cy,dx,dy,bx,by) == 0):
    flag = True
    if (min(ax,bx) <= max(cx,dx) and min(cx,dx) <= max(ax,bx) and min(ay,by) <= max(cy,dy) and min(cy,dy) <= max(ay,by)):
        answer = 1
if (CCW(ax,ay,bx,by,cx,cy) * CCW(ax,ay,bx,by,dx,dy) <= 0 and CCW(cx,cy,dx,dy,ax,ay) * CCW(cx,cy,dx,dy,bx,by) <= 0):
    if not flag:
        answer = 1
print(answer)