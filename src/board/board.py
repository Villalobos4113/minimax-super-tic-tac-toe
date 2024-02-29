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
                string_builder += f"{i*3+j+1}  | {board[y_values[i]][y_values[j]]} | {board[y_values[i]][y_values[j]+1]} | {board[y_values[i]][y_values[j]+2]} |    | {board[y_values[i]+1][y_values[j]]} | {board[y_values[i]+1][y_values[j]+1]} | {board[y_values[i]+1][y_values[j]+2]} |    | {board[y_values[i]+2][y_values[j]]} | {board[y_values[i]+2][y_values[j]+1]} | {board[y_values[i]+2][y_values[j]+2]} |\n   +---+---+---+    +---+---+---+    +---+---+---+\n"
            string_builder += "\n   +---+---+---+    +---+---+---+    +---+---+---+\n" if i != 2 else ""
        
        return string_builder
    
    def make_move(self, position: str) -> bool:
        # Convert position to board index
        board = self.convert_position_to_index_board(position)
        if board == -1:
            return False

        # Convert position to position index
        position = self.convert_position_to_index(position)
        if position == -1:
            return False

        # Check if board and position are valid
        if self.current_sub_board != -1 and self.current_sub_board != board:
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

    def convert_position_to_index_board(self, position: str) -> int:
        if len(position) != 2:
            return -1
        letter_value = {"A": 0, "B": 0, "C": 0, "D": 1, "E": 1, "F": 1, "G": 2, "H": 2, "I": 2}
        number_value = {"1": 0, "2": 0, "3": 0, "4": 3, "5": 3, "6": 3, "7": 6, "8": 6, "9": 6}
        column = letter_value[position[0].upper()]
        row = number_value[position[1]]
        return row + column
    
    def is_position_free(self, board: int, position: int) -> bool:
        # Check if the position is in range
        if board in range(9) and position in range(9):
            # Check if the position is free
            return self.sub_boards[board][position] == 0
        raise Exception("Board and position must be in range 0-8")
    
    def check_win_sub(self, sb_index: int):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]

        board = self.sub_boards[sb_index]

        # Check for winning combinations
        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] != 0:
                self.main_board[sb_index] = board[combo[0]]
                return True
        
        return False

    def check_win_main(self) -> tuple[bool, int]:
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]

        # Check for winning combinations
        for combo in winning_combinations:
            if self.main_board[combo[0]] == self.main_board[combo[1]] == self.main_board[combo[2]] != 0:
                return True, self.main_board[combo[0]]
        
        return False, 0