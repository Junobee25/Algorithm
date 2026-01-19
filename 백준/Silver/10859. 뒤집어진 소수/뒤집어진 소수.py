input = input()

def transferNumber(n_string):
    change_map = {
        '0' : '0',
        '1' : '1',
        '2' : '2',
        '5' : '5',
        '8' : '8',
        '6' : '9',
        '9' : '6',
        '3' : 'false',
        '4' : 'false',
        '7' : 'false'
    }
    result = ''
    for i in n_string:
        if change_map[i] == 'false':
            return 'no'
        else :
            result += change_map[i]
    return result[::-1]

def miller_rabin_test(n, a, d, s):
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    
    for _ in range(s - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True
    return False

def isPrime(n):
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0: return False

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    bases = [2, 7, 61]

    for a in bases:
        if n <= a: break
        if not miller_rabin_test(n, a, d, s):
            return False
    return True
    
if transferNumber(input) == 'no':
    print('no')
else:
    if isPrime(int(input)) and isPrime(int(transferNumber(input))):
        print('yes')
    else:
        print('no')    