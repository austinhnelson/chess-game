import pygame
from constants import *
from board import Board
from pieces import Pawn

pygame.init()

WIDTH = HEIGHT = WINDOW_SIZE
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(SCREEN_CAPTION)
timer = pygame.time.Clock()

board = Board(BOARD_SIZE)
turn = 'white'

pieces = [
    Pawn(0, 1, 'black'), Pawn(1, 1, 'black'), Pawn(2, 1, 'black'), Pawn(3, 1, 'black'),
    Pawn(4, 1, 'black'), Pawn(5, 1, 'black'), Pawn(6, 1, 'black'), Pawn(7, 1, 'black'),
    Pawn(0, 6, 'white'), Pawn(1, 6, 'white'), Pawn(2, 6, 'white'), Pawn(3, 6, 'white'),
    Pawn(4, 6, 'white'), Pawn(5, 6, 'white'), Pawn(6, 6, 'white'), Pawn(7, 6, 'white'),
]

run = True
while run:
    timer.tick(FRAME_RATE)
    screen.fill('dark gray')

    board.draw_board(screen)

    for piece in pieces:
        piece.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            for piece in pieces:
                if piece.rect.collidepoint(mousePos) and piece.color == turn:
                    piece.selected = True
                else:
                    piece.selected = False
        elif event.type == pygame.MOUSEBUTTONUP:
            for piece in pieces:
                piece.selected = False

    pygame.display.flip()
pygame.quit()