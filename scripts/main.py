"""
This is a Tank Game based on PocketTanks, made in Python 3 using Pygame and Pymunk for physics
"""

import sys
import pygame
import pymunk
import pymunk.pygame_util

# CLASS AND FUNCTION IMPORTS
from ground import Ground
from tank import Tank
from text import text


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
        self.player2 = Tank("blue")

        # Setup code
        self.current_player = self.player1
        self.moves_left = 200

        self.player1.body._set_position((100, 250))
        self.player2.body._set_position((width-136, 250))

        # Add game objects to space
        self.ground.add_to_space(self.space)
        self.player1.add_to_space(self.space)
        self.player2.add_to_space(self.space)

    def input(self, keys):
        tank = self.current_player
        body = self.current_player.body
        speed = Tank("ehhh").vertices[2][0] * 2.3333333333
        rot_speed = 1

        # Tank Movement
        if body.velocity[1] < 1 and self.moves_left > 0:
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                body.velocity = speed, body.velocity[1]
                self.moves_left -= 1
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                body.velocity = -speed, body.velocity[1]
                self.moves_left -= 1

        # Turret Rotation
        if keys[pygame.K_q] or keys[pygame.K_COMMA]:
            tank.turn_turret(rot_speed)
        if keys[pygame.K_e] or keys[pygame.K_PERIOD]:
            tank.turn_turret(-rot_speed)

    def logic(self):
        print(self.moves_left)
        self.player1.update_rect()
        self.player2.update_rect()

    def render(self):
        self.win.fill(self.background)

        # Render Game Objects
        self.ground.render(self.win)
        self.player1.render(self.win)
        self.player2.render(self.win)

        # Render UI Elements
        text(
            self.win,
            "Player 1: " + str(self.player1.score),
            25,
            (255, 255, 255),
            (80, 30)
        )

        text(
            self.win,
            "Player 2: " + str(self.player2.score),
            25,
            (255, 255, 255),
            (self.win_size[0] - 80, 30)
        )

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
