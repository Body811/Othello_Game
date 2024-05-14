from Player import Player
from Board import Board
from AiPlayer import AiPlayer
import random
import time
class Othello:
    def __init__(self):
        self.board = Board()
        self.player = Player("B")
        self.computer = AiPlayer("W")
        self.turn = "B"
        
    
    
    def switch_turn(self):
        if self.turn == "B":
            self.turn = "W"
        else:
            self.turn = "B"
    
    
    
                    
 
    
    def play(self):
        
        choice = input("Choose A difficulty\n1.Easy\n2.Medium\n3.Hard\n>>")
        if choice == '1':
            difficulty = 1  # Easy
        elif choice == '2':
            difficulty = 3  # Medium
        elif choice == '3':
            difficulty = 5  # Hard
        else:
            difficulty = 1  #default is easy
        
            
        
        self.board.display()
        flag = False
        while not self.board.is_finished(self.player, self.computer):
            if self.turn == "B":
                flag = False
                print("It black's turn")
                valid_moves = self.board.get_valid_moves(self.player)
                if valid_moves:
                    row, col = self.player.get_move() 
                    if (self.board.make_move(row, col, self.player, valid_moves)):
                        self.board.display()
                        self.switch_turn()
                    else:
                        print("Invalid move! Try again.")
                else:
                    flag = True
                    print("You Dont have valid Moves. Your turn is Skiped")
                    self.switch_turn()
            else:
                print("It is white's turn")
                valid_moves = self.board.get_valid_moves(self.computer)
                if valid_moves:
                    row, col = self.computer.get_move(self.board, difficulty, self.player) 

                    if(self.board.make_move(row, col, self.computer, valid_moves)):
                        self.board.display()
                        self.switch_turn()
                    else:
                        print("Computer made an invalid move")
                else:
                    if flag == True:
                        print("Both players have no valid moves")
                        break;
                    print("You Dont have valid Moves. Your turn is Skiped")
                    self.switch_turn()

                    

                    
        print(f"  {'-'*10} GAME OVER {'-'*10}\n")
        black_count, white_count = self.board.count_disks()
        if black_count > white_count:
            print("Black won!")
        elif white_count > black_count:
            print("White won!")
        else:
            print("It is a tie")


othello = Othello()

othello.play()