import pygame
import sys
from swarm_camera.ImageProcessing import process_image
from swarm_camera.Visualization import Board

def draw(screen):
    screen.fill((32,34,38))
    board.draw(screen)
    pygame.display.flip()

def update():
    (x, y) = pygame.mouse.get_pos()
    board.setGoalAll(x, y)
    board.update()

pygame.init()
windowsize = (600, 500)
screen = pygame.display.set_mode(windowsize)
timer = pygame.time.Clock()
board = Board.Board(windowsize[0], windowsize[1], 50)

while 1:
    # Event getter loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    update()
    draw(screen)
    pygame.time.delay(3)