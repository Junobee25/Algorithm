# 기차의 수 명령의 수
n,m = map(int,input().split())
# 이차원 배열에 기차 넣기(0번째 기차 ~ n-1번째기차)
train_list = [[0]*20 for _ in range(n)]

# i번째 기차에 x번째 좌석에 사람을 태운다
# 이미 사람이 타있다면, 아무런 행동을 하지 않음
def one(i,x):
    if train_list[i-1][x-1] == 1:
        pass
    else:
        train_list[i-1][x-1] = 1

def two(i,x):
    if train_list[i-1][x-1] == 0:
        pass
    else:
        train_list[i-1][x-1] = 0
def three(i):
    train_list[i-1].insert(0,0)
    train_list[i-1].pop()

def four(i):
    train_list[i-1].pop(0)
    train_list[i-1].append(0)


for i in range(m):
    check = list(map(int,input().split()))
    if check[0] == 1:
        one(check[1],check[2])
    elif check[0] == 2:
        two(check[1],check[2])
    elif check[0] == 3:
        three(check[1])
    else:
        four(check[1])
cnt = 0
check_train = []
for i in train_list:
    if i not in check_train:
        check_train.append(i)
        cnt += 1

print(cnt)