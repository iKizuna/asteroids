from constants import *
import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = rotation
        self.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
        if (self.position.x < -self.radius or 
            self.position.x > SCREEN_WIDTH + self.radius or 
            self.position.y < -self.radius or 
            self.position.y > SCREEN_HEIGHT + self.radius):
            self.kill()  # Remove the shot if it goes off-screen