# 문제이해
# 기술을 특정 조건을 만족할 때만 사용 가능
# 조건 => 점수 N일 때 자릿수를 기준으로 점수 N을 반으로 나누어
# 왼쪽 부분의 각 자리수 합과 오른쪽 부분의 각 자리수 합이 동일한 상황
# 즉 짝수길이의 숫자열을 반으로 잘랐을 때 왼쪽과 오른쪽의 합이 같으면 LUCKY
# 다르면 READY

# 입력 (10<=N<=99,999,999)

# 접근
# 숫자열을 슬라이싱으로 2부분으로 나눈다면 sum함수로 확인

number = list(map(int,input()))

# 반으로 자르기
flag = len(number)//2

if sum(number[0:flag]) == sum(number[flag:]):
    print("LUCKY")
else:
    print("READY")