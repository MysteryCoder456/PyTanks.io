import pygame
import pymunk


class Ground:
    """Class for making the Ground/Terrain in the game

    Arguments:
        window_width {int} -- width of the game window
        window_height {int} -- height of the game window
    """

    def __init__(self, width, height, window_size):
        self.vertices = [
            (0, 0),
            (width, 0),
            (width, height),
            (0, height)
        ]

        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Poly(self.body, self.vertices)
        self.color = (0, 170, 0)

        self.body.position = 0, window_size[1] - height
        self.update_rect()

    def add_to_space(self, space):
        space.add(self.body, self.shape)

    def update_rect(self):
        pos = self.body.position
        size = self.vertices[2]
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

    def render(self, window):
        pygame.draw.rect(window, self.color, self.rect)
