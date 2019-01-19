import math
import random

class Particle:

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
        self.velocity_mag = 0.5 # Speed of the particles

    def setGoal(self, x,y):
        self.goalx = x
        self.goaly = y

    def goto(self):
        # TODO: Track the particle to a specific destination

        if abs(self.goalx - self.x) < 0.0000000001:
            angle = math.atan2((self.goaly - self.y), (0.0000000001))

            self.vy = self.velocity_mag * (math.sin(angle))

            self.vx = self.velocity_mag * (math.cos(angle))
        else:
            if self.distanceToGoal() > 10:
                angle = math.atan2((self.goaly - self.y), (self.goalx - self.x))

                #noise_factor = self.velocity_mag / 10
                noise_factor = 0
                noise_1 = random.uniform(-noise_factor , noise_factor)
                noise_2 = random.uniform(-noise_factor , noise_factor)

                self.vy = self.velocity_mag * (math.sin(angle)) + noise_1

                self.vx = self.velocity_mag * (math.cos(angle)) + noise_2

    # Return the distance to the goal
    def distanceToGoal(self):
        return ((self.x - self.goalx) ** 2 + (self.y - self.goaly) ** 2) ** 0.5

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
