"""
This is a Tank Game based on PocketTanks, made in Python 3 using Pygame and Pymunk for physics
"""

import sys
import pygame
import pymunk
import pymunk.pygame_util

# CLASS IMPORTS
from ground import Ground
from tank import Tank


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
        self.space.gravity = 0, 500

        # Create game objects
        self.ground = Ground(self.win_size[0], 150, self.win_size)
        self.player1 = Tank("red")
        self.player1.body._set_position((100, 250))

        # Add game objects to space
        self.ground.add_to_space(self.space)
        self.player1.add_to_space(self.space)



    def input(self, keys):
        p1_body = self.player1.body

        speed = 40

        if keys[pygame.K_d]:
            p1_body.velocity = speed, p1_body.velocity[1]
        elif keys[pygame.K_a]:
            p1_body.velocity = -speed, p1_body.velocity[1]
        else:
            p1_body.velocity = 0, p1_body.velocity[1]

    def logic(self):
        # print(self.player1.body.position)
        pass

    def render(self):
        self.win.fill(self.background)

        self.player1.render(self.win)
        self.ground.render(self.win)

        pygame.display.flip()


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

        game.input(pygame.key.get_pressed())
        game.logic()
        game.render()

        delta_time = 1./fps
        game.space.step(delta_time)


if __name__ == "__main__":
    main()
    sys.exit()
