length = sorted(list(map(int, input().split())))
if length[0] + length[1] > length[2]:
    print(sum(length))
else:
    print((length[0] + length[1]) * 2 - 1)