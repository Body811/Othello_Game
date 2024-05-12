class Player:
    def __init__(self, color):
        self.color = color
        self.diskNum = 30
        
    def get_move(self):
        r = int(input("Enter row (0-7): "))
        c = int(input("Enter column (0-7): "))
        return r, c