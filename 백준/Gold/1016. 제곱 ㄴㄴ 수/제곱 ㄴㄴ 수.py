import math

min, max = map(int,input().split())


results = []
square_number = [i**2 for i in range(2, int(max ** (1/2)) + 1)]

#validation list
validation = [1] * (max - min + 1)

for square in square_number:
    cur_idx = (math.ceil(min / square) * square) - min
    while cur_idx <= max - min:
        validation[cur_idx] = 0
        cur_idx += square
        

result = sum(validation)
print(result)