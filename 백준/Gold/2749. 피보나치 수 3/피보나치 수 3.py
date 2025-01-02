n = int(input())

p = 1500000
m = 1000000
fibo = [0] * (n%p + 1)
fibo[1] = 1
 
for i in range(2, n%p + 1):
    fibo[i] = (fibo[i-1] + fibo[i-2]) % m 

print(fibo[n%p])
