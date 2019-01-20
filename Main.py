import pygame
import sys
from Visualization import Board
import cv2 as cv
from ImageProcessing import process_image as process
from Distribution import RandomDistribution
import random
import threading
import _thread
import queue
import time
import numpy

# Helper Functions
def draw(screen):
    screen.fill((32, 34, 38)) # Reset screen
    board.draw(screen) # Draw function
    pygame.display.update() # Update screen

def update():
    # (x, y) = pygame.mouse.get_pos()
    # board.setGoalAll(x, y)
    board.update()

def update_draw(screen):
    # print("Retrieved: " + str(random_goals))
    draw(screen)
    update()


def updateBoardGoals(board, random_distr):
    board.chooseGoals(random_distr)  # Choose goals, using specific distribution


def calc_goals(cap, random_queue, inv_queue, board):
    while 1:
        small = getFrame(cap)
        gray = process.grayImage(small)
        #thresh = process.thresholdImage(gray, 1, 1)
        #eroded = process.morphTrans(thresh, 1, 2, 1)
        #contour = process.contourImage(gray)
        edge = process.edgeDetection(gray)
        inv_image = process.invertImage(edge)  # black is lines
        inv_queue.put(inv_image)
        random_goals = random_distr.createRandomDistribution(inv_image)

        #cv.imshow("Live", inv)

        random_queue.put(random_goals)

        board.chooseGoals(random_goals)  # Choose goals, using specific distribution

        #print("Added to queue")
        time.sleep(0.2)

def getFrame(cap):
    ret, frame = cap.read()
    width, height, color = frame.shape
    x_min = int(width/4)
    x_max = int(width - (width/4))
    y_min = int(height/4)
    y_max = int(height - (height/4))
    section = frame[x_min:x_max, y_min:y_max]
    return section

# Initializations
pygame.init()
timer = pygame.time.Clock()
cap = cv.VideoCapture(0)
small = getFrame(cap)
height, width, channels = small.shape
swarm_number = 1000
board = Board.Board(width, height, swarm_number)
screen = pygame.display.set_mode([width, height])
random_goals = queue.Queue()
inv_image = queue.Queue()
random_distr = RandomDistribution.RandomDistribution(swarm_number)

t = _thread.start_new_thread(calc_goals, (cap,random_goals, inv_image, board))

cv.imshow("Live", inv_image.get())
# Main Loop
while 1:

    # Event getter loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # random_goals = calc_goals(cap)


    if cv.waitKey(1) & 0xFF == ord('y'):
        print("Exiting")
        cv.destroyAllWindows()
        break

    # print("Queue len" + str(random_goals.qsize()))
    update_draw(screen)
    # print("Goal queue size: " + str(random_goals.qsize()))
    # pygame.time.delay(2)

