"""
This is a Tank Game based on PocketTanks, made in Python 3 using Pygame and Pymunk for physics
"""

import sys
import pygame
import pymunk
import pymunk.pygame_util

# CLASS IMPORTS
from ground import Ground


class PyTanksIO:
    """
    Main class that contains most of the code for the game
    """

    def __init__(self, width, height, title):
        # Window initializing code
        self.win_size = width, height
        self.win = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        self.running = True
        self.background = (0, 0, 0)

        # Pymunk initializing code
        pymunk.pygame_util.positive_y_is_up = False
        self.space = pymunk.Space()
        self.space.gravity = 0, 100

        # Game initializing code
        self.ground = Ground(self.win_size[0], 150, self.win_size)

        self.ground.add_to_space(self.space)

    def logic(self):
        pass

    def render(self):
        self.win.fill(self.background)

        self.ground.render(self.win)

        pygame.display.update()


def main():
    """
    The main function that starts the entire game.
    Only modify this function if you know what you're doing.
    """

    pygame.init()
    game = PyTanksIO(1048, 700, "PyTanks.io")
    clock = pygame.time.Clock()
    fps = 60

    while True:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        game.logic()
        game.render()


if __name__ == "__main__":
    main()
    sys.exit()
