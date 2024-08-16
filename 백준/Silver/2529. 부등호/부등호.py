from itertools import permutations
n = int(input())
arr = list(map(str, input().split()))

number_list = [i for i in range(0, 10)]
result_list = []
for sub_list in permutations(number_list, len(arr) + 1):
    for idx in range(len(sub_list) - 1):
        if arr[idx] == ">":
            if sub_list[idx] < sub_list[idx + 1]:
                break
        else:
            if sub_list[idx] > sub_list[idx + 1]:
                break
    else:
        result_list.append(sub_list)
result_list.sort()
print(''.join(map(str,result_list[-1])))
print(''.join(map(str,result_list[0])))