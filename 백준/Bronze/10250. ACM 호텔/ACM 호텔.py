T = int(input())

for i in range(T):
    A, B, C = map(int, input().split())
    num = C//A + 1
    stack = C % A
    if C % A == 0:  # h의 배수이면,
        num = C//A
        stack = A
    print(f'{stack*100+num}')