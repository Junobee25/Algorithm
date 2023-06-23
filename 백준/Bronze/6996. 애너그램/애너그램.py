n = int(input())
for _ in range(n):
    A,B = input().split()
    if sorted(A) == sorted(B):
        print(A + " & " + B + " are anagrams." )
    else:
        print(A + " & " + B + " are NOT anagrams." )