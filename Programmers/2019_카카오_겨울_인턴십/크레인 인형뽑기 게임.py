def pickDoll(board, idx):
    for i in range(len(board)):
        if board[i][idx - 1] != 0:
            doll = board[i][idx - 1]
            board[i][idx - 1] = 0
            return board, doll
    return board, None

def isSame(doll, stackDoll):
    return doll == stackDoll

def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        board, doll = pickDoll(board, move)
        if doll == None:
            continue
        if stack:
            if isSame(doll, stack[-1]):
                answer += 2
                stack.pop()
            else:
                stack.append(doll)
        else:
            stack.append(doll)
    return answer


if __name__ == "__main__":
    print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))