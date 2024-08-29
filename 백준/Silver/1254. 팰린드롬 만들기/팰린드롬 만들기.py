import sys

word = str(sys.stdin.readline().rstrip("\n"))

for i in range(len(word)):
    if word[i:] == word[i:][::-1]:
        print(len(word) + i)
        break