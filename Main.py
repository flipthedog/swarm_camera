import pygame
import sys
from swarm_camera.Visualization import Board
import cv2 as cv
from swarm_camera.ImageProcessing import process_image as process
import random

def draw(screen):
    screen.fill((32,34,38))
    board.draw(screen)
    pygame.display.update()

def update(distr_goals):
    # (x, y) = pygame.mouse.get_pos()
    # board.setGoalAll(x, y)
    board.chooseGoals(distr_goals)
    board.update()


def find_black_pixels(image):
    return_arr = []

    height, width = image.shape

    for i in range(0, width):

        for j in range(0, height):

            if image[j][i] == 0:
                pixel = [i,j]
                return_arr.append(pixel)

    return return_arr


pygame.init()
timer = pygame.time.Clock()
cap = cv.VideoCapture(0)
ret, frame = cap.read()
small = cv.resize(frame, (0,0), fx=0.5, fy=0.5)
height, width, channels = small.shape
swarm_number = 500
board = Board.Board(width, height, swarm_number)
screen = pygame.display.set_mode([width, height])


def random_distribution(black_pixel_array):

    return_arr = []

    length = len(black_pixel_array)

    for i in range(0, swarm_number):

        randomnum = random.randint(0,length - 1)

        return_arr.append(black_pixel_array[randomnum])

    return return_arr

i = 0

while 1:

    # Event getter loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if i % 5 == 0:
        ret, frame = cap.read()
        small = cv.resize(frame, (0, 0), fx=0.5, fy=0.5)
        gray = process.grayImage(small)
        #thresh = process.thresholdImage(gray, 1, 1)
        #eroded = process.morphTrans(thresh, 1, 2, 1)
        #contour = process.contourImage(gray)
        edge = process.edgeDetection(gray)
        inv = process.invertImage(edge) # black is lines

        cv.imshow("Live", inv)

        black_pixels = find_black_pixels(inv)
        distr_goals = random_distribution(black_pixels)

    i += 1
    if cv.waitKey(1) & 0xFF == ord('y'):
        print("Exiting")
        cv.destroyAllWindows()
        break

    update(distr_goals)
    draw(screen)
    #pygame.time.delay(2)

