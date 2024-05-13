from Othello import Othello, Game

choice = input("Choose A difficulty\n1.Easy\n2.Medium\n3.Hard\n>>")
if choice == '1':
    difficulty = 1  # Easy
elif choice == '2':
    difficulty = 3  # Medium
elif choice == '3':
    difficulty = 5  # Hard
else:
    difficulty = 1  # default is easy

game = Game(difficulty)
game.run()