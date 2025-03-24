import pygame
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    # overriding the draw method
    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius, 2)



    # overriding the update method
    def update(self, dt):
        self.x += self.velocity.x * dt
        self.y += self.velocity.y * dt