n,m = map(int,input().split())
string = input()
a,c,g,t = map(int,input().split())


tmp_string = string[:m]
cnt = 0
dic = {'A' : 0, 'C' : 0, 'G' : 0, 'T' : 0}

for i in tmp_string:
    dic[i] += 1

if dic['A'] >= a and dic['C'] >= c and dic['G'] >= g and dic['T'] >= t:
    cnt += 1
 



for i in range(n-m):
    dic[string[i]] -= 1
    dic[string[m + i]] += 1
    if dic['A'] >= a and dic['C'] >= c and dic['G'] >= g and dic['T'] >= t:
        cnt += 1

print(cnt)
 