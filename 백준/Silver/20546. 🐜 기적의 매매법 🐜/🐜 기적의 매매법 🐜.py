money = int(input())

stock = list(map(int,input().split()))
jun_cnt = 0
sung_cnt = 0
increse = [0]*14
decrease = [0]*14
jun_money = money
sung_money = money
jun_result = 0
sung_result = 0




for i in range(1,len(stock)):
    if stock[i-1] < stock[i]:
        increse[i] = increse[i-1] + 1
    elif stock[i-1] > stock[i]:
        decrease[i] = decrease[i-1] + 1

for i in range(len(stock)):
    if jun_money >= stock[i]:
        k = jun_money//stock[i]
        jun_cnt += k
        jun_money -= stock[i] * k
    if i == 13:   
        jun_result = stock[i]*jun_cnt + jun_money


for i in range(len(stock)):
    if decrease[i] >= 3 and sung_money >= stock[i]:
        k = sung_money//stock[i]
        sung_cnt += k
        sung_money -= stock[i]*k
    if increse[i] >=3:
        sung_money += stock[i]*sung_cnt

    if i == 13:
        sung_result = stock[i]*sung_cnt + sung_money

if jun_result > sung_result:
    print("BNP")
elif jun_result < sung_result:
    print("TIMING")
elif jun_result == sung_result:
    print("SAMESAME")

