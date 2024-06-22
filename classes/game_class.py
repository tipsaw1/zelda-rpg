from game.settings import *

class Game:
    # Screen info
    current_screen = 1
    display_surface = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    running = True

    def start_menu(self):
        self.display_surface.fill("black")