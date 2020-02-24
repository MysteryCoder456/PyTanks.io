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

        mass = 10
        self.body = pymunk.Body(mass, body_type=pymunk.Body.DYNAMIC)
        self.body.moment = pymunk.moment_for_poly(mass, self.vertices)
        self.body.center_of_gravity = (width/2, height/2)

        self.shape = pymunk.Poly(self.body, self.vertices)
        self.shape.elasticity = 0.3
        self.shape.friction = 1.0

        self.update_rect()

        if team == "red":
            self.color = (200, 40, 40)
            self.direction = 0
        elif team == "blue":
            self.color = (40, 40, 200)
            self.direction = 180

        self.score = 0

    def turn_cannon(self, angle):
        self.direction += angle

    def add_to_space(self, space):
        space.add(self.body, self.shape)

    def update_rect(self):
        pos = self.body.position
        size = self.vertices[2]
        self.rect = (pos[0], pos[1], size[0], size[1])

    def render(self, window):
        pygame.draw.rect(window, self.color, self.rect)
