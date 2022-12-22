import sys
input = sys.stdin.readline

# 최대 기준 숫자설정
maxNum = -999999

# N개의 자연수 입력
N = int(input())

# N개의 수 리스트로 만듦기
number_list = list(input().split())
new_list = []
k = 0

# 1. 자연수의 자릿수의 합을 구하는 함수
def digit_sum(x):
    b = 0
    for i in x:
        b += int(i)
    return b

# 2. 각자리수의 합을 new_list에 담기
for i in number_list:
    new_list.append(digit_sum(i))

# 3. 각 자리수의 합이 같을 경우 고려해 continue문으로 중복안되게 입력순으로 인덱스를 k에 저장
for i in range(len(number_list)):
    if new_list[i] == maxNum :
        continue
    if new_list[i] > maxNum :
        maxNum = new_list[i]
        k = i

print(number_list[k])

# 구현순서 = 2-> 3-> 1