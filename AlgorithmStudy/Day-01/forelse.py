for i in range(1, 10):
    print(i)
    if i == 5:
        break   # break 되면 else문 실행x
else:
    print(11)

for i in range(1,10):
    print(i)
    if i > 15:
        break  # for 문이 정상적으로 실행되면 else문 실행o
else:
    print(11)

