n,m = map(int,input().split())
from itertools import combinations
arr = list(map(int,input().split()))


result = 9999999
flag = 0
for i in combinations(arr,3):
    if sum(i) - m <= 0 and abs(sum(i) - m) <= result:
        result = abs(sum(i)-m) 
        flag = sum(i)
print(flag)