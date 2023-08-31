n, m = map(int,input().split())

number_list = list(map(int,input().split()))

end = 0
current_sum = number_list[0]
min_length = n + 1

for start in range(len(number_list)):
    while (current_sum < m and end < n - 1):
        end += 1
        current_sum += number_list[end]
    if current_sum >= m:
        if (end-start + 1) < min_length:
            min_length = end - start + 1

        current_sum -= number_list[start]

if min_length > n:
    print(0)
else:
    print(min_length)
    
