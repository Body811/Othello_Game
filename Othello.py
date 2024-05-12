from Player import Player
from Board import Board
from AiPlayer import AiPlayer
import random
import time
class Othello:
    def __init__(self):
        self.board = Board()
        self.player = Player("B")
        self.computer = Player("W")
        self.turn = "B"
        
    def isfinshed(self):
        if (not any(self.board.is_valid_move(r, c, 'B') or self.board.is_valid_move(r, c, 'W') for r in range(8) for c in range(8)) 
            or self.player.diskNum == 0 or self.computer.diskNum == 0):
            return True
        
        return False
    
    def switch_turn(self):
        if self.turn == "B":
            self.turn = "W"
        else:
            self.turn = "B"
    
    
    def get_valid_moves(self, player):
        valid_moves = []
        for row in range(8):
            for col in range(8):
                if self.board.is_valid_move(row, col, player.color):
                    valid_moves.append((row, col))
        return valid_moves
                    
 
    
    def play(self):
        self.board.display()
        flag = False
        while not self.isfinshed():
            if self.turn == "B":
                flag = False
                print("It black's turn")
                valid_moves = self.get_valid_moves(self.player)
                if valid_moves:
                    row, col = self.player.get_move() #comment this if you want it to play it self
                    # row, col = random.choice(valid_moves) # Uncomment this if you want it to play it self
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
                valid_moves = self.get_valid_moves(self.computer)
                if valid_moves:
                    row, col = self.computer.get_move() #comment this if you want it to play it self
                    # row, col = random.choice(valid_moves) # Uncomment this if you want it to play it self
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
                    
            # time.sleep(1)  # Uncomment this if you want it to play it self
                    
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