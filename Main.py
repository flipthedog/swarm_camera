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

def update(random_distr):
    # (x, y) = pygame.mouse.get_pos()
    # board.setGoalAll(x, y)
    board.chooseGoals(random_distr) # Choose goals, using specific distribution
    board.update()

def update_draw(screen, random_queue):
    random_goals = random_queue.get()
    # print("Retrieved: " + str(random_goals))
    draw(screen)
    update(random_goals)

    if random_queue.empty():
        random_queue.put(random_goals)


def calc_goals(cap, random_queue, inv_queue):
    while 1:
        ret, frame = cap.read()
        small = cv.resize(frame, (0, 0), fx=0.5, fy=0.5)
        gray = process.grayImage(small)
        # thresh = process.thresholdImage(gray, 1, 1)
        # eroded = process.morphTrans(thresh, 1, 2, 1)
        # contour = process.contourImage(gray)
        edge = process.edgeDetection(gray)
        inv_image = process.invertImage(edge)  # black is lines
        inv_queue.put(inv_image)
        random_goals = random_distr.createRandomDistribution(inv_image)

        #cv.imshow("Live", inv)

        random_queue.put(random_goals)

        #print("Added to queue")
        time.sleep(0.2)

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
random_goals = queue.Queue()
inv_image = queue.Queue()
random_distr = RandomDistribution.RandomDistribution(swarm_number)

try:
    None
    # t = threading.Thread(target=calc_goals, args=(cap, random_goals))
except:
    print("Error: Unable to start goal calculation thread")

t = _thread.start_new_thread(calc_goals, (cap,random_goals, inv_image))


# Main Loop
while 1:

    # Event getter loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # random_goals = calc_goals(cap)

    cv.imshow("Live", inv_image.get())
    if cv.waitKey(1) & 0xFF == ord('y'):
        print("Exiting")
        cv.destroyAllWindows()
        break

    # print("Queue len" + str(random_goals.qsize()))
    update_draw(screen, random_goals)
    # print("Goal queue size: " + str(random_goals.qsize()))
    # pygame.time.delay(2)

