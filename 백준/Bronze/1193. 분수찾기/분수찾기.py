N = int(input())

line = 0
max_location = 0

while N > max_location :
    line += 1
    max_location += line

diff = max_location - N

if line%2 == 0:
    top = line - diff
    bottom = diff + 1
else:
    top = diff + 1
    bottom = line - diff
print(str(top)+"/"+str(bottom))