import pygame
from constants import *

class Board:
    def __init__(self, board_size):
        self.board_size = board_size

    def draw_board(self, screen):
        for y in range(self.board_size):
            for x in range(self.board_size):
                color = TILE_COLOR_1 if (y + x) % 2 == 0 else TILE_COLOR_2
                pygame.draw.rect(screen, color, pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
