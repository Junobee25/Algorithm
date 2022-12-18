# 1부터 N까지 홀수 출력하기
n = int(input())
for i in range(n+1):
    if i % 2 != 0:
        print(i)
# 1부터 N까지의 합 구하기
n = int(input())
sum = (n*(n+1))/2
print(sum)
# 1부터 N까지의 합 구하기
mysum = 0
for i in range(1,n+1):
    mysum += i
print(mysum)
# N의 약수 출력하기
n = int(input())
for i in range(1,n+1):
    if n % i == 0 :
        print(i , end=" ") # end 이용하여 옆으로 출력 

