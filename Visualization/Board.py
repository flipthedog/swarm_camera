import pygame
from swarm_camera.Visualization import Particle
import random

class Board:

    def __init__(self, width, height, particle_number):
        self.swarm = []
        self.width = width
        self.height = height
        self.particle_number = particle_number
        # Create particle_number particles
        for i in range(0, particle_number):
            self.addswarmparticle()


    def draw(self, screen):
        color = pygame.Color(255, 0, 0, 255)

        for particle in self.swarm:
            # print("Drawing at: " + str(particle.x) + ", " + str(particle.y))
            pygame.draw.circle(screen, color, [int(particle.x), int(particle.y)], 2, 0)

    def update(self):

        for particle in self.swarm:
            particle.update()

    def addswarmparticle(self):
        x = random.randint(0, self.width)
        y = random.randint(0, self.height)

        p = Particle.Particle(x, y, self.width, self.height)
        self.swarm.append(p)

    def setRandomGoals(self):

        for particle in self.swarm:
            vel_mag = particle.velocity_mag
            particle.vx = random.uniform(-1, 1) * vel_mag
            particle.vy = random.uniform(-1, 1) * vel_mag

    def setGoalAll(self,x ,y):

        for particle in self.swarm:
            particle.setGoal(x, y)