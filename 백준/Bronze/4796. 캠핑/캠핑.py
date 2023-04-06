circle = 0
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break 
    circle += 1
    cnt = (v // p) * l  # 최대 이용 가능한 횟수
    cnt += min(v % p, l)  # 나머지 남은 일수 중 l일 이하만큼 이용 가능
    print(f"Case {circle}:", cnt)