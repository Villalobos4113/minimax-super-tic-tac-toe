class Board:
    def __init__(self, start_player=1):
        '''
        Initialize the board with the given start player
        :param start_player: int, 1 for player, -1 for AI
        '''

        self.main_board = [0] * 9  # 0 for empty, 1 for player, -1 for AI
        self.sub_boards = [[0] * 9 for _ in range(9)]  # 0 for empty, 1 for player, -1 for AI
        self.current_player = start_player if start_player in (-1, 1) else 1 # 0 for empty, 1 for player, -1 for AI
        self.current_sub_board = -1
    
    def to_string(self):
        board = [[" "] * 9 for _ in range(9)]

        for i in range(9):
            if self.main_board[i] == 0:
                for j in range(9):
                    board[i][j] = "X" if self.sub_boards[i][j] == 1 else "O" if self.sub_boards[i][j] == -1 else " "
            else:
                for j in range(9):
                    board[i][j] = "X" if self.main_board[i] == 1 else 'O' if self.main_board[i] == -1 else " "
        
        y_values = (0, 3, 6)

        string_builder = "     A   B   C        D   E   F        G   H   I\n   +---+---+---+    +---+---+---+    +---+---+---+\n"
        for i in range(3):
            for j in range(3):
                string_builder += f"{i*3+j+1}  | {board[i][y_values[j]]} | {board[i][y_values[j]+1]} | {board[i][y_values[j]+2]} |    | {board[i+1][y_values[j]]} | {board[i+1][y_values[j]+1]} | {board[i+1][y_values[j]+2]} |    | {board[i+2][y_values[j]]} | {board[i+2][y_values[j]+1]} | {board[i+2][y_values[j]+2]} |\n   +---+---+---+    +---+---+---+    +---+---+---+\n"
            string_builder += "\n   +---+---+---+    +---+---+---+    +---+---+---+\n" if i != 2 else ""
        
        return string_builder