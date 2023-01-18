N = int(input())
row = list(map(int,input().split()))
new_row = list(set(row))

new_row.sort() # set sort 를 통해 작은수 큰수를 나눔 해당 숫자가 몇번째 위치인지만 알면 됨 그게 상대적 크기순서임

hash = {}

for i in range(len(new_row)):
    hash[new_row[i]] = i

for i in row:
    print(hash[i],end=" ")