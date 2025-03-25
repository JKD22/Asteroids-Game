import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity=None):
        super().__init__(x, y, radius)
        self.position = self.get_position()
        if velocity is None:
            # Create a default velocity or random velocity
            self.velocity = pygame.math.Vector2(random.uniform(20, 60))  # Configure as needed
        else:
            self.velocity = velocity
    # overriding the draw method
    def draw(self, screen):
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.circle(screen, random_color, (self.position.x, self.position.y), int(self.radius), 2)

    # overriding the update method
    def update(self, dt):
        self.x += self.velocity.x * dt
        self.y += self.velocity.y * dt
        self.position = self.get_position()

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # create two smaller asteroids
        random_angle = random.uniform(0, 360)
        #calculate new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        #calculate new velocity
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        # scale up velocities
        new_velocity1 *= 1.2
        new_velocity2 *= 1.2
        #create new asteroids
        Asteroid(self.position.x, self.position.y, new_radius, new_velocity1)
        Asteroid(self.position.x, self.position.y, new_radius, new_velocity2)