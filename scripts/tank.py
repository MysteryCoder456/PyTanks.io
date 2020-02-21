import pygame
import pymunk


class Tank:
    """Class for creating a Tank

    Arguments:
        pos {tuple} -- Starting position of the Tank
        team {str} -- Team name of the Tank
    """

    def __init__(self, pos, team):
        width, height = 50, 20
        self.vertices = [
            (0, 0),
            (width, 0),
            (width, height),
            (0, height)
        ]

        self.body = pymunk.Body(50)
        self.body.position = pos
        self.shape = pymunk.Poly(self.body, self.vertices)

        # Rect for rendering
        self.rect = self.update_rect()

        if team == "red":
            self.color = (200, 40, 40)
        elif team == "blue":
            self.color = (40, 40, 200)

    def add_to_space(self, space):
        space.add(self.body, self.shape)

    def update_rect(self):
        pos = self.body.position
        size = self.vertices[2]
        return pygame.Rect(pos[0], pos[1], size[0], size[1])

    def render(self, window):
        pygame.draw.rect(window, self.color, self.rect)
