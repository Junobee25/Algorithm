import sys
input = sys.stdin.readline
N = int(input())
dice_case = [list(map(int,input().split())) for _ in range(N)]
price = []

# 주사위 계산 값 갱신해주는 함수 (함수 안의 로직도 반복되는거 같은데 굳이 함수 써야하나?)
def Calculator(x):
    if len(list(set(x))) == 1:
       price.append(10000 + list(set(x))[0] * 1000)
    elif (x[0] == x[1]) or (x[0] == x[2]) or (x[1] == x[2]):
        if x[0] == x[1] :
            price.append(1000 + x[0] * 100)
        elif x[0] == x[2] :
            price.append(1000 + x[0] * 100)
        elif x[1] == x[2]:
            price.append(1000 + x[1] * 100)
    elif len(list(set(x))) == 3:
        price.append(max(list(set(x))) * 100)
    return price

# dice_case의 원소를 계산기에 넣어줌
for i in dice_case:
    Calculator(i)

print(max(price))