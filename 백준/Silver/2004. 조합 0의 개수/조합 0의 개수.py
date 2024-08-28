def count_number(input_number, number):
    k = input_number
    cnt = 0
    while k > 1:
        cnt += k//number
        k //= number
    return cnt

a, b = map(int, input().split())

number_of_two_inc_de = count_number(a, 2)
number_of_five_inc_de = count_number(a, 5)


number_of_two_inc_mo = count_number(b,2) + count_number(a - b, 2)
number_of_five_inc_mo = count_number(b,5) + count_number(a - b, 5)

result1 = number_of_two_inc_de - number_of_two_inc_mo
result2 = number_of_five_inc_de - number_of_five_inc_mo

print(min(result1, result2))