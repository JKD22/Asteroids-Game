import pygame
import time
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

    
    def get_position(self):
        return pygame.Vector2(self.x, self.y)

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(screen, WHITE, self.triangle(), 2)
        pygame.draw.circle(screen, (255, 0, 0), (int(self.position.x), int(self.position.y)), self.radius, 1)



    def update(self, dt):
        # sub-classes must override
        pass
    
    def collision(self, other):
        #get positions
        self_pos = self.position
        other_pos = other.position

        distance = self_pos.distance_to(other_pos)

        if distance <= self.radius + other.radius:
            return True
        return False