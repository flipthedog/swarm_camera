import math
import random
import pygame
import pygame.gfxdraw

class Particle():

    def __init__(self, x, y, width, height):

        self.width = width
        self.height = height

        self.x = x
        self.y = y
        self.vy = 0
        self.vx = 0
        self.ax = 0
        self.ay = 0
        self.goalx = x
        self.goaly = y
        self.velocity_mag = 5  # Speed of the particles

    def setGoal(self, x, y):
        self.goalx = x
        self.goaly = y

    def goto(self):

        if abs(self.goalx - self.x) < 0.0000000001:
            angle = math.atan2((self.goaly - self.y), 0.0000000001)

            self.vy = self.velocity_mag * (math.sin(angle))

            self.vx = self.velocity_mag * (math.cos(angle))

        else:
            if self.distanceToGoal() > self.velocity_mag:
                angle = math.atan2((self.goaly - self.y), (self.goalx - self.x))

                # noise_factor = self.velocity_mag / 10
                noise_factor = 0
                noise_1 = random.uniform(-noise_factor , noise_factor)
                noise_2 = random.uniform(-noise_factor , noise_factor)

                self.vy = self.velocity_mag * (math.sin(angle)) + noise_1

                self.vx = self.velocity_mag * (math.cos(angle)) + noise_2
            else:
                self.vy = 0
                self.vx = 0

    # Return the distance to the goal
    def distanceToGoal(self):
        return abs(self.x - self.goalx) + abs(self.y - self.goaly)

    def update(self):
        self.goto()

        self.vx += self.ax
        self.vy += self.ay

        # Steer back into the board
        # TODO Replace this with a more elegant solution
        if self.x > self.width or self.x < 0:
            self.vx = -self.vx

        # TODO same here
        if self.y < 0 or self.y > self.height:
            self.vy = -self.vy


        self.x += self.vx
        self.y += self.vy
