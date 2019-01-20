import pygame
from Visualization import Particle
import random

class Board:

    def __init__(self, width, height, particle_number):
        self.swarm = pygame.sprite.Group()
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
            pygame.draw.circle(screen, color, [int(particle.x), int(particle.y)], 3, 0)

    def update(self):

        self.swarm.update()

    def addswarmparticle(self):
        x = random.randint(0, self.width)
        y = random.randint(0, self.height)

        p = Particle.Particle(x, y, self.width, self.height)

        self.swarm.add(p)

    def setRandomGoals(self):

        for particle in self.swarm:
            vel_mag = particle.velocity_mag
            particle.vx = random.uniform(-1, 1) * vel_mag
            particle.vy = random.uniform(-1, 1) * vel_mag

    def setGoalAll(self,x ,y):

        for particle in self.swarm:
            particle.setGoal(x, y)

    def chooseGoals(self, goals):

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
