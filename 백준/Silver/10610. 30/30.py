# 문제이해
# 주어진 수의 조합들 중 30의 배수가 될 수 있는 
# 가장 큰 수

# 접근
# 입력 100000
# 내림차순 정렬해서 30으로 나누어떨어지면 그게 답
# 나누어 떨어지지 않으면 30의 배수가 될 수 없음

number_str = list(input())
number_str.sort(reverse=True)
number = ''
for i in number_str:
    number += i

if (int(number)%30) != 0:
    print(-1)
else:
    print(int(number))


