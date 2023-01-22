T = int(input())
def OTT(v):
    if v == 1:
        return 1
    if v == 2:
        return 2
    if v == 3:
        return 4
    else:
        return OTT(v-3) + OTT(v-2) + OTT(v-1)

for i in range(T):
    n = int(input())
    print(OTT(n))