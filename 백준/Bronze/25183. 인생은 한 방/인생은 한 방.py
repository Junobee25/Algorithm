
length = int(input())
alpa = ['A','B','C','D','E','F','G','H',
        'I','J','K','L','M','N','O','P',
        'Q','R','S','T','U','V','W','X',
        'Y','Z']
is_win = [1]*length

lotto = input()

for i in range(1,len(lotto)):
    k = alpa.index(lotto[i-1]) - alpa.index(lotto[i])
    if abs(k) == 1:
        is_win[i] = is_win[i-1] + 1

if max(is_win) >= 5:
    print('YES')
else:
    print('NO')


