from board.board import Board
from settings import clean

import os
from time import sleep


class Game:
    def __init__(self):
        self.board = None
        self.game_mode = -1
        self.ai_1 = None
        self.ai_2 = None
        self.players = None

        self.config()

    def config(self):
        while True:
            os.system(clean)
            print('=' * 40)
            print("Welcome to Ultimate Tic Tac Toe!")
            print()
            print("1. Play Player vs Player")
            print("2. Play Player vs AI")
            print("3. Play AI vs AI")
            print()
            print('=' * 40)
            choice = input("Enter your choice: ")
            if choice == '1':
                self.game_mode = 0
                self.board = Board()
                self.players = ['Player 1', 'Player 2']
                break
            elif choice == '2':
                self.game_mode = 1
                self.players = ['Player', 'AI']
                # self.a1_1
                while True:
                    os.system(clean)
                    print('=' * 40)
                    print()
                    print('1. Player first')
                    print('2. AI first')
                    print()
                    print('=' * 40)
                    choice = input("Enter your choice: ")
                    if choice == '1':
                        self.board = Board()
                        break
                    elif choice == '2':
                        self.board = Board(-1)
                        break
                    else:
                        print("Invalid choice. Please try again.")
                        sleep(3)
                break
            elif choice == '3':
                self.game_mode = 2
                self.board = Board()
                self.players = ['AI 1', 'AI 2']
                # self.ai_1
                # self.ai_2
                break
            else:
                print("Invalid choice. Please try again.")
                sleep(3)

    def play(self):
        winned, winner = self.board.check_win_main()
        boards = {0: 'A-C 1-3', 1: 'C-F 1-3', 2: 'G-I 1,3', 3: 'A-C 4-6', 4: 'C-F 4-6', 5: 'G-I 4-6', 6: 'A-C 7-9', 7: 'C-F 7-9', 8: 'G-I 7-9'}

        while not winned:
            os.system(clean)
            print('='*40)
            print()
            print(self.board.to_string())
            print()
            print('='*40)
            print()
            print('    ' + self.players[0] if self.board.current_player == 1 else self.players[1])
            print()
            
            

                
game = Game()
game.play()