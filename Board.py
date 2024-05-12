import os

class Board:
    def __init__(self):
        self.board = [[' ']*8 for _ in range(8)]
        self.board[3][3] = self.board[4][4] = 'W'
        self.board[3][4] = self.board[4][3] = 'B'

        
    def display(self):
        # os.system('cls')
        horizontal_border = "+---"*8+"+"
        print("    0   1   2   3   4   5   6   7  ")
        print("  +" + "-"*31 + "+")
        for i, row in enumerate(self.board):
            print(f"{i} | " + " | ".join(row) + " |")
            print("  +" + "-"*31 + "+")
        print()

        
    def is_valid_move(self, row, col, player_color):
        if not (0 <= row < 8) or not (0 <= col < 8) or self.board[row][col] != ' ':
            return False

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] != player_color and self.board[r][c] != ' ':
                    return True
        return False
        
    def make_move(self, row, col, player):

        if not self.is_valid_move(row, col, player.color):
            return False
        
        self.board[row][col] = player.color
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] != player.color and self.board[r][c] != ' ':
                r += dr
                c += dc
            if 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == player.color:
                r, c = row + dr, col + dc
                while self.board[r][c] != player.color:
                    self.board[r][c] = player.color
                    r += dr
                    c += dc
        player.diskNum -= 1
        return True
    def count_disks(self):
        black_count = sum(row.count('B') for row in self.board)
        white_count = sum(row.count('W') for row in self.board)
        return black_count, white_count    


# def test_board():
#     board = Board()
#     current = "B"
#     # Display initial board
#     print("Initial Board:")
#     board.display_board()

#     # Test is_valid_move method
#     while True:
#         if current == "B":
#             print("Black's Turn")
#         else:
#             print("White's Turn")

#         r = int(input("Enter row (0-7): "))
#         c = int(input("Enter column (0-7): "))

#         if board.make_move(r, c, current):
#             print("invalid move")    
#             if current == "B":
#                 current = "W"
#             else:
#                 current = "B"    
#             board.display_board()     
#         else:
#             print("invalid move")    

# test_board()