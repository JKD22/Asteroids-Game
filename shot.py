import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, WHITE

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
    
    def update(self, dt):
        # Update position based on velocity
        self.x += self.velocity.x * dt
        self.y += self.velocity.y * dt
    
    def draw(self, screen):
        # Override the parent's draw method with our own implementation
        position = self.get_position()
        pygame.draw.circle(screen, WHITE, (int(position.x), int(position.y)), self.radius, 1)