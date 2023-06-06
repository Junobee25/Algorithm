def solution(order):
    answer = 0
    max_value = 0
    stack = []
    for i in range(len(order)):
        if order[i] > max_value:
            for j in range(max_value + 1, order[i]):
                stack.append(j)
            answer += 1
            max_value = order[i]
        elif order[i] < max_value:
            if stack[-1] == order[i]:
                answer += 1
                stack.pop()
            else:
                break
     
    return answer