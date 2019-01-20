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

        self.color = [255,255,255]

    def setGoal(self, x, y):
        self.goalx = x
        self.goaly = y

    def goto(self):

        if abs(self.goalx - self.x) < 0.0000000001:
            angle = math.atan2((self.goaly - self.y), 0.0000000001)

            self.vy = self.velocity_mag * (math.sin(angle))

            self.vx = self.velocity_mag * (math.cos(angle))

        else:
            distance = self.distanceToGoal()
            if distance > self.velocity_mag:

                color_scalar = (distance) / (self.height + self.width)

                g = int(255*color_scalar)
                r = int(255 - 255*color_scalar)-150

                #r = r*r
                g = g*g
                if r>255:
                    r = 255
                if g>255:
                    g = 255
                if r<0:
                    r = 0

                self.color = [255-r, 255-g, 255]

                angle = math.atan2((self.goaly - self.y), (self.goalx - self.x))

                # noise_factor = self.velocity_mag / 10
                noise_factor = 0
                noise_1 = random.uniform(-noise_factor , noise_factor)
                noise_2 = random.uniform(-noise_factor , noise_factor)

                slow_down_scale = 15
                slow_down_y = slow_down_scale * (abs(self.y - self.goaly) / self.height) + 0.1
                slow_down_x = slow_down_scale * (abs(self.x - self.goalx) / self.width) + 0.1

                self.vy = self.velocity_mag * (math.sin(angle)) * slow_down_y + noise_1

                self.vx = self.velocity_mag * (math.cos(angle)) * slow_down_x + noise_2
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

        if self.x > self.width:
            self.x = self.width
        else:
            self.x += self.vx

        if self.y > self.height:
            self.y = self.height
        else:
            self.y += self.vy
