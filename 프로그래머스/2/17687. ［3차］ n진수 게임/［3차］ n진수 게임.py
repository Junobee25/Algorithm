def solution(n, t, m, p):
    answer = ''
    
    base_conversion_list = make_integer_list(n)

    for i in range(p-1, len(base_conversion_list), m):
        answer += base_conversion_list[i]
        if (len(answer) >= t):
            break
            
    return answer


def base_conversion(n, q):
    rev_base = ''
    dchar = '0123456789ABCDEF'
    if q == 0:
        return '0'
    
    while q > 0:
        rev_base += dchar[q % n]
        q //= n

    return rev_base[::-1] 

def make_integer_list(n):
    base_conversion_list = []
    
    for i in range(0, 100001):
        for ele in base_conversion(n, i):
            base_conversion_list.append(ele)
            
    return base_conversion_list
