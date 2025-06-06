# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():

    dt = 0.0  # Delta time

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    # Create player at center of screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        dt = clock.tick(60) / 1000.0  # Get delta time in seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        player.update(dt)
    
        screen.fill((0, 0, 0))  # Fill screen with black
        player.draw(screen)  # Draw player
        pygame.display.flip()   # Update the display

    pygame.time.Clock().tick(60)  # Limit to 60 FPS
    pygame.quit()

if __name__ == "__main__":
    main()