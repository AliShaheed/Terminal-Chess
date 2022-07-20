
class Board:
    def __init__(self) -> None:
        self.board = [["| ", "   " ], ["---"]]

    def draw_board(self) -> str:
        row_element = 0
        row_str = ""
        buffer = True

        for _ in range(17):
            if buffer:
                for _ in range(14):
                    row_str += self.board[1][0]
                row_str += "\n"
                buffer = False
            else:
                for _ in range(17):
                    if row_element == 0:
                        row_str += self.board[0][0]
                        row_element += 1
                    elif row_element == 16:
                        row_str += self.board[0][0]
                        row_str += "\n"
                        row_element = 0
                        buffer = True
                    elif row_element % 2 == 0:
                        row_str += self.board[0][0]
                        row_element += 1
                    else:
                        row_str += self.board[0][1]
                        row_element += 1
        buffer = True   
        return row_str

chess = Board()
board = chess.draw_board()
print(board)




