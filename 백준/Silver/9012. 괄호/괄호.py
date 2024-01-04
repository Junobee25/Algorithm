import sys

T = int(sys.stdin.readline())
OPEN_BRACKET = "("
CLOSE_BRACKET = ")"
NO = "NO"
YES = "YES"

for _ in range(T):
    bracket_list = list(sys.stdin.readline().rstrip())
    stack = []

    if bracket_list[0] == CLOSE_BRACKET:
        print(NO)
        continue

    for idx in range(len(bracket_list)):
        if bracket_list[idx] == OPEN_BRACKET:
            stack.append(OPEN_BRACKET)
        else:
            if stack and stack[-1] == OPEN_BRACKET:
                stack.pop()
            else:
                stack.append(CLOSE_BRACKET)

    if not stack:
        print(YES)
    else:
        print(NO)