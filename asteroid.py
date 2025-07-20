import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        random_angle = random.uniform(20, 50)
        old_radius = self.radius
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            vector_a = self.velocity.rotate(random_angle)
            vector_b = self.velocity.rotate(-random_angle)
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            asteroid_a = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_a.velocity = vector_a * 1.2
            asteroid_b = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_b.velocity = vector_b * 1.2


        
