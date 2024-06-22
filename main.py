# Imports
import classes.game_class
from game.settings import *

# Initialize pygame
pygame.init()

# Create game instance
main_game = classes.game_class.Game()

# Clock variable
clock = pygame.time.Clock()

# Game loop
while main_game.running:
    # Events
    for event in pygame.event.get():
        # End loop upon red X
        if event.type == pygame.QUIT:
            main_game.running = False

    # Update screen
    pygame.display.flip()
    clock.tick(60)

# Close game
pygame.quit()