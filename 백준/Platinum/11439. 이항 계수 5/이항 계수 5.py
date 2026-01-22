import sys

def get_v_p(n, p):
    count = 0
    while n > 0:
        n //= p
        count += n
    return count

def solve():
    line = sys.stdin.readline()
    if not line:
        return
    n, k, m = map(int, line.split())

    if k < 0 or k > n:
        print(0)
        return
    if k == 0 or k == n:
        print(1 % m)
        return

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    primes = [i for i, prime in enumerate(is_prime) if prime]

    ans = 1
    for p in primes:
        exponent = get_v_p(n, p) - get_v_p(k, p) - get_v_p(n - k, p)
        if exponent > 0:
            ans = (ans * pow(p, exponent, m)) % m
            
    print(ans)

if __name__ == "__main__":
    solve()