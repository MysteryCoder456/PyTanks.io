import pygame
import pymunk


class Ground:
    """Class for making the Ground/Terrain in the game

    Arguments:
        window_width {int} -- Width of the game window.
        window_height {int} -- Height of the game window.
    """

    def __init__(self, width, height, window_size):
        # Vertices for the ground
        vertices = [
            (0, 0),
            (width, 0),
            (width, height),
            (0, height)
        ]

        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.center_of_gravity = (width/2, height/2)

        self.shape = pymunk.Poly(self.body, vertices)
        self.shape.elasticity = 0.3
        self.shape.friction = 0.7

        self.color = (0, 170, 0)

        # Place ground on bottom of the screen
        self.body.position = 0, window_size[1] - height

        # Rect for rendering
        pos = self.body.position
        size = vertices[2]
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

    def add_to_space(self, space):
        space.add(self.body, self.shape)

    def render(self, window):
        pygame.draw.rect(window, self.color, self.rect)
