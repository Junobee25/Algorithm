import sys
input = sys.stdin.readline


def binary_search(target,data):
    start = 0
    end = len(data) - 1
    
    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return True
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    

n = int(input().rstrip())

number_list = []

for _ in range(n):
    number_list.append(int(input().rstrip()))

left = []

for i in range(n):
    for j in range(i,n):
        left.append(number_list[i] + number_list[j])

left = list(set(left))
left.sort()
max_val = 0

for i in range(1,n):
    for j in range(n-1):
        if binary_search(number_list[i] - number_list[j], left):
            max_val = max(max_val,number_list[i])

print(max_val) 