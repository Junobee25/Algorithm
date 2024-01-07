
def solution(board, moves):
    answer = 0
    """
    기능 요구사항
    1. moves 배열의 인덱스 정보를 이용해 인형을 뽑는다.
    2. 맨 위의 인형을 뽑고 stack에 삽입, 뽑은 자리를 빈 칸으로 만든다.
    3. stack에 넣을 때 인형이 일치하면 제거하고 일치하지 않으면 넣는다.
    4. 사라진 인형의 개수를 카운트한다.
    """
    stack = []
    
    for i in moves:
        move = 0
        while True:
            if move == len(board):
                break
            if board[move][i-1]:
                if stack:
                    if stack[-1] == board[move][i-1]:
                        stack.pop()
                        board[move][i-1] = 0
                        answer += 2
                    else:
                        stack.append(board[move][i-1])
                        board[move][i-1] = 0
                else:
                    stack.append(board[move][i-1])
                    board[move][i-1] = 0
                break
            move += 1
    return answer