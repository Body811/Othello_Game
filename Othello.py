import sys
import pygame as pg
from Player import Player
from Board import Board
from AiPlayer import AiPlayer


Vec2 = pg.math.Vector2
WIN_SIZE = 600
CELL_SIZE = WIN_SIZE // 8


class Game:
    def __init__(self, difficulty):
        pg.init()
        self.screen = pg.display.set_mode([WIN_SIZE] * 2)
        self.clock = pg.time.Clock()
        self.othello = Othello(self, difficulty)

    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_event()
            self.othello.play()
            pg.display.update()
            self.clock.tick(60)


class Othello:
    def __init__(self, game, difficulty):
        self.board = Board(game)
        self.player = Player("B")
        self.computer = AiPlayer("W")
        self.turn = "B"
        self.game = game
        self.count = 0
        self.count2 = 0
        self.difficulty = difficulty

    def isfinished(self):
        return not any(self.board.is_valid_move(r, c, 'B') or self.board.is_valid_move(r, c, 'W') for r in range(8) for c in range(8)) \
               or self.player.diskNum == 0 or self.computer.diskNum == 0

    def switch_turn(self):
        self.turn = "W" if self.turn == "B" else "B"

    def get_valid_moves(self, player):
        valid_moves = []
        for row in range(8):
            for col in range(8):
                if self.board.is_valid_move(row, col, player.color):
                    valid_moves.append((row, col))
        return valid_moves

    def play(self):
        self.board.display()
        if not self.isfinished():
            self.board.print_caption(self.turn)
            flag = False
            if self.turn == "B":
                flag = False
                valid_moves = self.get_valid_moves(self.player)
                if valid_moves:
                    temp = self.player.get_move()
                    if temp is not None:
                        self.count2 = 0
                        row, col = temp  # Pass the board instance to player's get_move() method
                        if self.board.make_move(row, col, self.player, valid_moves):
                            self.board.display()
                            self.switch_turn()
                            count2 = 0
                        else:

                            if self.count2 == 0:
                                # print("Invalid move! Try again.")
                                self.count2 = 1
                else:
                    flag = True
                    if self.turn == "B":
                        current = "Black"
                    else:
                        current = "White"
                    if not self.isfinished():
                        print(current + " don't have valid moves. " + "Your turn is skipped")
                        self.switch_turn()
            else:
                valid_moves = self.get_valid_moves(self.computer)
                if valid_moves:
                    temp = self.computer.get_move(self.board, self.difficulty, self.player)
                    if temp is not None:
                        row, col = temp
                        self.count2 = 0
                        if self.board.make_move(row, col, self.computer, valid_moves):
                            self.board.display()
                            self.switch_turn()
                        else:
                            if self.count2 == 0:
                                # print("Computer made an invalid move")
                                self.count2 = 1
                    else:
                        print("temp is none\n")
                else:
                    if flag:
                        print("Both players have no valid moves")
                    if self.turn == "B":
                        current = "Black"
                    else:
                        current = "White"
                    if not self.isfinished():
                        print(current+" don't have valid moves. " + "Your turn is skipped")
                        self.switch_turn()
        else:
            if self.count == 0:

                print(f"{'-' * 10} GAME OVER {'-' * 10}\n")
                self.count = 1
                black_count, white_count = self.board.count_disks()
                if black_count > white_count:
                    print("Black won!")
                    pg.display.set_caption(f'player Black Won!')
                    return
                elif white_count > black_count:
                    print("White won!")
                    pg.display.set_caption(f'player White Won!')
                    return
                else:
                    print("It's a tie")
                    pg.display.set_caption(f'Tie!')
                    return
