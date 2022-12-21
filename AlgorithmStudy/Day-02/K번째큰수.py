'''import sys
input = sys.stdin.readline
n,k = map(int,input().split())

number_List = list(map(int,input().split())) # 문자열 '1234'
sum_List = []
for i in number_List:
    second_List = number_List.remove(i)
    for j in second_List:
        third_List = second_List.remove(j)
        for k in third_List:
            sum_List.append(i+j+k)


sum_List = sorted(set(sum_List))
print(sum_List[-k])
'''


# 카드를 뽑을 때마다 뽑은 카드는 다음 반복문에서 배제를 시켜야함
# -> 뽑을때마다 해당 값을 remove() 함수로 제거하고 새로운 변수에 할당 하려고 시도함
# .remove() 시 반환값이 NonType 이기때문에 TypeError: 'NoneType' object is not iterable 발생 -> 할당이 안됨

import sys
input = sys.stdin.readline
n, k = list(map(int,input().split()))
number_List = list(map(int,input().split()))
sum_List = []

for i in range(n):
    for j in range(i+1,n):
        for m in range(j+1,n):
            sum_List.append(number_List[i]+number_List[j]+number_List[m])

sum_List = sorted(set(sum_List))
print(sum_List[-k])

# for문은 처음 인덱스를 기준으로 순서대로 돌아감
# 2,3중 for문의 인덱스를 각각 +1 해주면 따로 제거할 필요없이 중복 제거해서 참조










