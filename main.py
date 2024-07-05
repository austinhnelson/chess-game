import pygame
from constants import *
from board import Board

pygame.init()

WIDTH = HEIGHT = WINDOW_SIZE
screen = pygame.display.set_mode([WIDTH, HEIGHT])

pygame.display.set_caption(SCREEN_CAPTION)

timer = pygame.time.Clock()

board = Board(BOARD_SIZE)

run = True
while run:
    timer.tick(FRAME_RATE)
    screen.fill('dark gray')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    board.draw_board(screen)

    pygame.display.flip()
pygame.quit()