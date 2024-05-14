import pygame as pg

Vec2 = pg.math.Vector2
WIN_SIZE = 600
CELL_SIZE = WIN_SIZE // 8


class Player:
    def __init__(self, color):
        self.color = color
        self.diskNum = 30

    def get_move(self):
        current_cell = Vec2(pg.mouse.get_pos()) // CELL_SIZE
        col, row = map(int, current_cell)
        left_click = pg.mouse.get_pressed()[0]

        if left_click:
            return row, col
        else:
            return None
