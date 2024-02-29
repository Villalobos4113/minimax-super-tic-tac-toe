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