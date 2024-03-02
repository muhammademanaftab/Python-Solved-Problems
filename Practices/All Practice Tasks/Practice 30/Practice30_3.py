def draw_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=' ')
        print()

def is_valid(board, i, j):
    if i < 0 or i >= 3 or j < 0 or j >= 3 or board[i][j] != '-':
        return False
    return True

def take_and_place_valid_input(board, mark):
    while True:
        i, j = map(int, input("Enter input row and column separated by space: ").split())
        if is_valid(board, i, j):
            board[i][j] = mark
            return

def check_win(b):
    if b[0][0] != '-' and b[0][0] == b[0][1] == b[0][2]:
        return True
    if b[1][0] != '-' and b[1][0] == b[1][1] == b[1][2]:
        return True
    if b[2][0] != '-' and b[2][0] == b[2][1] == b[2][2]:
        return True
    if b[0][0] != '-' and b[0][0] == b[1][0] == b[2][0]:
        return True
    if b[0][1] != '-' and b[0][1] == b[1][1] == b[2][1]:
        return True
    if b[0][2] != '-' and b[0][2] == b[1][2] == b[2][2]:
        return True
    if b[0][0] != '-' and b[1][1] == b[2][2] == b[0][0]:
        return True
    if b[0][2] != '-' and b[1][1] == b[0][2] == b[2][0]:
        return True
    return False

def main():
    board = [['-' for _ in range(3)] for _ in range(3)]
    turn = 'A'
    total_turns = 0

    while total_turns < 9:
        draw_board(board)
        take_and_place_valid_input(board, turn)
        if check_win(board):
            break
        if turn == 'A':
            turn = 'B'
        else:
            turn = 'A'
        total_turns += 1
    if total_turns == 9:
        print("Draw")
    elif turn == 'A':
        print("Congratulations, Player A won the game")
    else:
        print("Congratulations, Player B won the game")

main()
