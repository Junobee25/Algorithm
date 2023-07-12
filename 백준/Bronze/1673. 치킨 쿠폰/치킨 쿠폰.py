def calc(coupon, k, chicken):
    if coupon < k:
        chicken += coupon
        return chicken
    new_coupon = coupon //k + coupon % k
    chicken += coupon // k * k
    return calc(new_coupon, k, chicken)
 
while True:
    try:
        coupon, k = map(int, input().split())
        chicken = 0
        chicken = calc(coupon, k, chicken)
        print(chicken)
    except EOFError:
        break