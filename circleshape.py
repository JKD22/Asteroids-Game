import pygame
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

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

        print(f"Player position: {self_pos}, radius: {self.radius}")
        print(f"Asteroid position: {other_pos}, radius: {other.radius}")
        print(f"Distance: {distance}, Sum of radii: {self.radius + other.radius}")

        if distance < self.radius + other.radius:
            return True
        return False