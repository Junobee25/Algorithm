def onoff(num):
    if num == 0:
        return 1
    elif num == 1:
        return 0


T = int(input())

switch = list(map(int, input().split()))
P = int(input())
for i in range(P):
    sex, number = map(int, input().split())
    if sex == 1:
        for i in range(1,T+1):
            if i%number == 0:
                switch[i-1] = onoff(switch[i-1])

    elif sex == 2:
        k = min(number-1,T-number)
        if k == number-1:
            switch[number-1] = onoff(switch[number-1])
            for i in range(0,k):
                if number == 1:
                    switch[number-1] = onoff(switch[number-1])
                    switch[number-1] = onoff(switch[number-1])
                elif switch[number-2-i] == switch[number+i]:
                    
                    switch[number-2-i] = onoff(switch[number-2-i])
                    switch[number+i] = onoff(switch[number+i])
                else:
                    switch[number-1] = onoff(switch[number-1])
                    switch[number-1] = onoff(switch[number-1])
                    break

        elif k == T-number:
            switch[number-1] = onoff(switch[number-1])
            for i in range(0,k):
                if number == T:
                    switch[number-1] == onoff(switch[number-1])
                    switch[number-1] = onoff(switch[number-1])
                elif switch[number-2-i] == switch[number+i]:
                    switch[number-2-i] = onoff(switch[number-2-i])
                    switch[number+i] = onoff(switch[number+i])
                else:
                    switch[number-1] = onoff(switch[number-1])
                    switch[number-1] = onoff(switch[number-1])
                    break
for i in range(1,T+1):
    print(switch[i-1],end=" ")
    if i%20==0:
        print()