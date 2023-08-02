# 득표율이 5% 이상인지 고려 해야 함
x = int(input())
p = int(input())

# [[(나눈값,알파벳)],[(나눈값,알파벳)]]
part_arr = []
for i in range(p):
    flag = 'F'
    alpa, cnt = input().split()
    cnt = int(cnt)
    # 0.05 미만 투표율 버리기
    if (cnt / x) < 0.05:
        continue
    # 나눈값과 참가자 튜플로 저장
    else:
        flag = 'T'
        for j in range(1,15):
            part_arr.append((cnt/j,alpa,flag))


# 내림차순 정렬
part_arr.sort(reverse=True)

# 14등까지 참가자에 따른 토큰값 카운트하기 위해 딕셔너리 선언
cnt_dict = {}
# 14번째 튜플 값까지 카운트
for i in range(14):
    if part_arr[i][1] not in cnt_dict:
        cnt_dict[part_arr[i][1]] = 1
    else:
        cnt_dict[part_arr[i][1]] += 1

for i in range(len(part_arr)):
    if part_arr[i][2] == 'T' and part_arr[i][1] not in cnt_dict:
        cnt_dict[part_arr[i][1]] = 0



# 알파벳 오름차순 정렬하기 위해 딕셔너리에서 꺼내서 리스트에 append
result_arr = []
for k,v in cnt_dict.items():
    result_arr.append((k,v))

# 오름 차순 정렬
result_arr.sort()

# 원하느 값 출력
for result in result_arr:
    print(result[0],result[1])
