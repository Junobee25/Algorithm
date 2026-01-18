import sys

input = sys.stdin.read

def is_prime(n):
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

def miller_rabin_test(n, a, d, s):
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True

    for _ in range(s - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True
    return False

def solve():
    input_data = input().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    areas = map(int, input_data[1:])
    
    invalid_count = 0
    for s in areas:
        target = 2 * s + 1
        if is_prime(target):
            invalid_count += 1
            
    print(invalid_count)

if __name__ == "__main__":
    solve()