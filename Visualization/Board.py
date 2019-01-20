import pygame
from Visualization import Particle
import random
import time
import pygame

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

        for particle in self.swarm:
            color = pygame.Color(particle.color[0], particle.color[1], particle.color[2], 255)
            # print("Drawing at: " + str(particle.x) + ", " + str(particle.y))
            pygame.gfxdraw.aacircle(screen, int(particle.x), int(particle.y), 5, color)
            pygame.gfxdraw.filled_circle(screen, int(particle.x), int(particle.y), 5, color)

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

    def chooseGoals(self, goals):
        start = time.time()
        for particle in self.swarm:
            partx = particle.x
            party = particle.y

            shortest_d = 999999
            shortest_goal = goals[0]

            newGoals = []

            for goal in goals:
                x = goal[0]
                y = goal[1]

                dist = abs(partx - x) + abs(party - y)

                if dist < shortest_d:
                    newGoals.append(shortest_goal)
                    shortest_d = dist
                    shortest_goal = goal
                else:
                    newGoals.append(goal)

            particle.setGoal(shortest_goal[0], shortest_goal[1])
            goals = newGoals
        end = time.time()

        # print("Time taken: " + str(end - start))