import pygame
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",(self.position[0], self.position[1]),self.radius,2)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius == ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            angle = random.uniform(20,50)
            vector_one = self.velocity.rotate(angle)
            vector_two = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteriod_one = Asteroid(self.position[0],self.position[1],new_radius)
            asteriod_two = Asteroid(self.position[0],self.position[1],new_radius)
            asteriod_one.velocity = vector_one * 1.2
            asteriod_two.velocity = vector_two * 1.2
            self.kill()
