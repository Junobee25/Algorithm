arr = []

for _ in range(3):
    arr.append(list(map(int,input().split())))

def direct_vector(point_a, point_b):
    return (point_b[0] - point_a[0], point_b[1] - point_a[1])

def cross_product(vector_a, vector_b):
    return vector_a[0]* vector_b[1] - vector_a[1]*vector_b[0]


def CCW(P1,P2,P3):
    vector_a = direct_vector(P1, P2)
    vector_b = direct_vector(P2, P3)
    k = cross_product(vector_a, vector_b)

    if k > 0:
        return 1
    elif k < 0 :
        return -1
    return 0

print(CCW(arr[0],arr[1],arr[2]))