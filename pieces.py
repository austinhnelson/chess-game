from abc import abstractmethod
from constants import *
import pygame

class Piece:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.selected = False
        self.color = color

    @abstractmethod
    def get_valid_moves(self):
        pass

    @abstractmethod
    def draw(self):
        pass

class Pawn(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.image = pygame.image.load(f'assets/images/{color}-pawn.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = pygame.Rect(self.x * 100, self.y * 100, self.image.get_width(), self.image.get_height())

    def get_valid_moves(self):
        moves = []
        if self.color == 'white':
            if self.y == 6:
                moves = [(self.x, self.y - 1), (self.x, self.y - 2)]
            else:
                moves = [(self.x, self.y-1)]
        else:
            if self.y == 1:
                moves = [(self.x, self.y + 1), (self.x, self.y + 2)]
            else:
                moves = [(self.x, self.y+1)]
        
        return moves

    def draw(self, screen):
        screen.blit(self.image, (self.x * self.image.get_width(), self.y * self.image.get_height()))
        if self.selected:
            pygame.draw.circle(screen, BLACK, (self.x * self.image.get_width() + 50, self.y * self.image.get_height() + 50), 50, 3)
            valid_moves = self.get_valid_moves()
            for move in valid_moves:
                move_x, move_y = move
                pygame.draw.circle(screen, (0, 255, 0), (move_x * self.image.get_width() + 50, move_y * self.image.get_height() + 50), 15)

