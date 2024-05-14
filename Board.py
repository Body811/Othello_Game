import os
import pygame as pg

WIN_SIZE = 600
CELL_SIZE = WIN_SIZE // 8
Empty = ' '
Vec2 = pg.math.Vector2


class Board:
    def __init__(self, game):
        self.board = [[' '] * 8 for _ in range(8)]
        self.board[3][3] = self.board[4][4] = 'W'
        self.board[3][4] = self.board[4][3] = 'B'
        self.field_image = self.get_scaled_image(path='resources/mygrid.gif', res=[WIN_SIZE] * 2)
        self.black = self.get_scaled_image(path='resources/black2.png', res=[CELL_SIZE] * 2)
        self.white = self.get_scaled_image(path='resources/white.png', res=[CELL_SIZE] * 2)
        self.game = game

    def draw(self):
        self.game.screen.blit(self.field_image, (0, 0))
        self.draw_objects()

    def draw_objects(self):
        for y, row in enumerate(self.board):
            for x, obj in enumerate(row):
                if obj != ' ':
                    self.game.screen.blit(self.black if obj == 'B' else self.white, Vec2(x, y) * CELL_SIZE)

    @staticmethod
    def get_scaled_image(path, res):
        img = pg.image.load(path).convert_alpha()
        return pg.transform.smoothscale(img, res)

    def print_caption(self, turn):
        player = ""
        if turn == "B":
            player = "Black"
        else:
            player = "White"
        pg.display.set_caption(f'it is {player} turn')

    def display(self):
        self.draw()

    def is_valid_move(self, row, col, player_color):
        if not (0 <= row < 8) or not (0 <= col < 8) or self.board[row][col] != ' ':
            return False
        # directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] != player_color and self.board[r][c] != ' ':
                while 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] != player_color and self.board[r][c] != ' ':
                    r += dr
                    c += dc
                if 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == player_color:
                    return True
        return False

    def make_move(self, row, col, player, valid_moves):

        if not (row, col) in valid_moves:
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

    def get_valid_moves(self, player):
        valid_moves = []
        for row in range(8):
            for col in range(8):
                if self.is_valid_move(row, col, player.color):
                    valid_moves.append((row, col))
        return valid_moves

    def is_finshed(self, player1, player2):
        if player1.diskNum == 0 or player2.diskNum == 0:
            return True

        if not any(self.get_valid_moves(player1)) and not any(self.get_valid_moves(player2)):
            return True

        return False

    def copy(self):
        new_board = Board(self.game)
        new_board.board = [row[:] for row in self.board]
        return new_board


