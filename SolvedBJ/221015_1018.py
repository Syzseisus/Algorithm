import sys

def start_color(board, color):
    count = 0
    for r in range(8):
        for c in range(8):
            if board[r][c] != color:
                count += 1
            if c != 7:
                color = "W" if color == "B" else "B"
    return count

def check_board(board):
    white_count = start_color(board, "W")
    black_count = start_color(board, "B")
    return min(white_count, black_count)

def main(board, N, M):
    count = 64        
    for r in range(N - 7):
        for c in range(M - 7):
            sub_board = [i[c:c+8] for i in board[r:r+8]]
            count = min(count, check_board(sub_board))
            if count == 0:
                return count

    return count


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    board = [sys.stdin.readline().rstrip() for _ in range(N)]
    print(main(board, N, M))