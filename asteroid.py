import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = (128, 128, 128)  # Gray color for the asteroid
        self.speed = 0.5  # Speed of the asteroid

    def move(self):
        self.x += self.speed
        if self.x > SCREEN_WIDTH + self.radius:
            self.x = -self.radius  # Wrap around to the left side

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        # Split the asteroid into two smaller ones if it is large enough
        if self.radius > ASTEROID_MIN_RADIUS:
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            random_angle = random.uniform(20,50)

            # Create two new velocity vectors diverging from the original
            velocity1 = self.velocity.rotate(random_angle) * 1.2
            velocity2 = self.velocity.rotate(-random_angle) * 1.2
            
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = velocity1
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = velocity2
            return [asteroid1, asteroid2]
            
        return []