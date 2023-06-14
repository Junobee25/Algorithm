n,f=input(),input()
k=int(n[:-2]+'00')

while True:
    if k%int(f)==0:
        break
    k+=1
k=str(k)
print(k[-2:])