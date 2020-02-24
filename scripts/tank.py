from math import radians, sin, cos, ceil
import pygame
import pymunk


class Tank:
    """Class for creating a Tank

    Arguments:
        pos {tuple} -- Starting position of the Tank
        team {str} -- Team name of the Tank
    """

    def __init__(self, team):
        # Size Ratio = 9:5
        width = 23
        height = width * 0.5555555556

        self.vertices = (
            (0, 0),
            (width, 0),
            (width, height),
            (0, height)
        )

        mass = width * 0.2777777778
        self.body = pymunk.Body(mass, body_type=pymunk.Body.DYNAMIC)
        self.body.moment = pymunk.moment_for_poly(mass, self.vertices)
        self.body.center_of_gravity = (width/2, height/2)

        self.shape = pymunk.Poly(self.body, self.vertices)
        self.shape.elasticity = 0.3
        self.shape.friction = 1.0

        self.update_rect()

        if team == "red":
            self.color = (200, 40, 40)
            self.direction = 135
        elif team == "blue":
            self.color = (40, 40, 200)
            self.direction = -135
        else:
            self.color = (200, 200, 200)
            self.direction = 0

        self.turret_size = width * 0.6944444444
        self.score = 0

    def turn_turret(self, angle):
        self.direction += angle

    def add_to_space(self, space):
        space.add(self.body, self.shape)

    def update_rect(self):
        pos = self.body.position
        size = self.vertices[2]
        self.rect = (pos[0], pos[1], size[0], size[1])

    def render(self, window):
        # Render Body
        pygame.draw.rect(window, self.color, self.rect)

        # Render Turret
        size = self.vertices[2]

        start_pos = (
            self.body.position[0] + size[0] / 2,
            self.body.position[1]
        )

        end_pos = (
            sin(radians(self.direction)) * self.turret_size + start_pos[0],
            cos(radians(self.direction)) * self.turret_size + start_pos[1]
        )
        pygame.draw.line(window, (100, 100, 100), start_pos, end_pos, ceil(size[0]*0.1388888889))
