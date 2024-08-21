## 잃는 체력 오름 차순 정렬
## 현재 체력에 차를 누적 + 기쁨을 누적 if 남은 체력 > 0 일때까지
## if 누적 기쁨보다 큰 기쁨이 나오면 + if 잃는 체력이 100이 아니면 교체
import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

arr = []

for i in range(n):
    arr.append((a[i], b[i]))
    
max_result = 0

for i in range(1, n + 1):
    for sub_list in combinations(arr,i):
        stemina = 0
        result = 0
        for k in range(len(sub_list)):
            stemina += sub_list[k][0]
            result += sub_list[k][1]
            
        if stemina < 100 and result > max_result:
            max_result = result
            
print(max_result)
          