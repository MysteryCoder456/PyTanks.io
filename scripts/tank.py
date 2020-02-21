import pygame
import pymunk


class Tank:
    """Class for creating a Tank

    Arguments:
        pos {tuple} -- Starting position of the Tank
        team {str} -- Team name of the Tank
    """

    def __init__(self, team):
        width, height = 36, 20  # Ratio = 9:5
        self.vertices = (
            (0, 0),
            (width, 0),
            (width, height),
            (0, height)
        )

        self.body = pymunk.Body(1, 1666, body_type=pymunk.Body.DYNAMIC)
        self.shape = pymunk.Poly(self.body, self.vertices)
        self.shape.elasticity = 0.3
        # self.shape.friction = 0.7

        if team == "red":
            self.color = (200, 40, 40)
        elif team == "blue":
            self.color = (40, 40, 200)

    def add_to_space(self, space):
        space.add(self.body, self.shape)

    def render(self, window):
        pos = self.body.position
        size = self.vertices[2]
        pygame.draw.rect(window, self.color, (pos[0], pos[1], size[0], size[1]))
