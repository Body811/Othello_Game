from Player import Player
from Board import Board
from AiPlayer import AiPlayer

class Othello:
    def __init__(self):
        self.board = Board()
        self.player = Player("B")
        self.computer = AiPlayer("W")
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
    
    
    def play(self):
        self.board.display()
        
        while not self.isfinshed():
            if self.turn == "B":
                print("It black's turn")
                row, col = self.player.get_move()
                if (self.board.make_move(row, col, self.player)):
                    self.board.display()
                    self.switch_turn()
                else:
                    print("Invalid move! Try again.")
            else:
                print("It is white's turn")
                row, col = self.computer.get_move()
                if(self.board.make_move(row, col, self.computer)):
                    self.board.display()
                    self.switch_turn()
                else:
                    print("Computer made an invalid move")
                    
                    
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