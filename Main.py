import pygame
import sys
from Visualization import Board
import cv2 as cv
from ImageProcessing import process_image as process
from Distribution import RandomDistribution
import random

# Helper Functions
def draw(screen):
    screen.fill((32, 34, 38)) # Reset screen
    board.draw(screen) # Draw function
    pygame.display.update() # Update screen

def update(random_distr):
    # (x, y) = pygame.mouse.get_pos()
    # board.setGoalAll(x, y)
    board.chooseGoals(random_distr) # Choose goals, using specific distribution
    board.update()

def calc_goals(cap):
    ret, frame = cap.read()
    small = cv.resize(frame, (0, 0), fx=0.5, fy=0.5)
    gray = process.grayImage(small)
    # thresh = process.thresholdImage(gray, 1, 1)
    # eroded = process.morphTrans(thresh, 1, 2, 1)
    # contour = process.contourImage(gray)
    edge = process.edgeDetection(gray)
    inv = process.invertImage(edge)  # black is lines
    random_goals = random_distr.createRandomDistribution(inv)
    cv.imshow("Live", inv)

    return random_goals

# Initializations
pygame.init()
timer = pygame.time.Clock()
cap = cv.VideoCapture(0)
ret, frame = cap.read()
small = cv.resize(frame, (0,0), fx=0.5, fy=0.5)
height, width, channels = small.shape
swarm_number = 500
board = Board.Board(width, height, swarm_number)
screen = pygame.display.set_mode([width, height])
background = pygame.display.set_mode([width, height])
background.fill((32, 34, 38))  # Reset screen

random_distr = RandomDistribution.RandomDistribution(swarm_number)

i = 0

# Main Loop
while 1:

    # Event getter loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if i % 10 == 0:

        random_goals = calc_goals(cap)

    i += 1

    if cv.waitKey(1) & 0xFF == ord('y'):
        print("Exiting")
        cv.destroyAllWindows()
        break

    update(random_goals)
    draw(screen)
    #pygame.time.delay(2)

