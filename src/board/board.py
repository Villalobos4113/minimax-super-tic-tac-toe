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
    
    def make_move(self, board: int, position: str) -> bool:
        # Check if board and position are valid
        if self.current_sub_board != -1 and self.current_sub_board != board:
            return False
        
        # Convert position to index
        position = self.convert_position_to_index(position)
        if position == -1:
            return False
        
        # Check if the position is free
        if self.is_position_free(board, position):
            # Make the move
            self.sub_boards[board][position] = self.current_player
            self.current_sub_board = position
            self.current_player *= -1
            return True
        
        return False
    
    def convert_position_to_index(self, position: str) -> int:
        if len(position) != 2:
            return -1
        letter_value = {"A": 0, "B": 1, "C": 2, "D": 0, "E": 1, "F": 2, "G": 0, "H": 1, "I": 2}
        column = letter_value[position[0].upper()]
        row = (int(position[1]) - 1) % 3
        return row * 3 + column
    
    def is_position_free(self, board: int, position: int) -> bool:
        # Check if the position is in range
        if board in range(9) and position in range(9):
            # Check if the position is free
            return self.sub_boards[board][position] == 0
        raise Exception("Board and position must be in range 0-8")