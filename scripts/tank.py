from math import sin, cos, ceil
from math import radians as rad
import pygame
import pymunk

# CLASS AND FUNCTION IMPORTS
from bullet import Bullet
from text import text


class Tank:
    """Class for creating a Tank

    Arguments:
        pos {tuple} -- Starting position of the Tank.
        team {str} -- Team name of the Tank.
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

        mass = width * 0.5555555556
        self.body = pymunk.Body(mass)
        self.body.moment = pymunk.moment_for_poly(mass, self.vertices)
        self.body.center_of_gravity = (width/2, height/2)

        self.shape = pymunk.Poly(self.body, self.vertices)
        self.shape.elasticity = 0.3
        self.shape.friction = 1.0

        if team == "red":
            self.color = (200, 40, 40)
            self.direction = 135
        elif team == "blue":
            self.color = (40, 40, 200)
            self.direction = 225
        else:
            self.color = (200, 200, 200)
            self.direction = 0

        self.turret_size = width * 0.6944444444
        self.score = 0
        self.fire_timer = 0
        self.fire_power = 50  # in percentage

        self.update()

    def shoot(self):
        tank_size = self.vertices[2]
        bullet_speed = self.fire_power * 12

        start_pos = self.turret_end_pos
        start_vel = (
            sin(rad(self.direction)) * bullet_speed,
            cos(rad(self.direction))*bullet_speed
        )
        radius = tank_size[0] * 0.2173913043

        return Bullet(start_pos, start_vel, radius)

    def turn_turret(self, angle):
        self.direction += angle
        if self.direction <= 0:
            self.direction = 359
        elif self.direction >= 360:
            self.direction = 1

    def add_to_space(self, space):
        space.add(self.body, self.shape)

    def update(self):
        if self.fire_power < 0:
            self.fire_power = 0
        elif self.fire_power > 100:
            self.fire_power = 100

        pos = self.body.position
        size = self.vertices[2]

        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

        self.turret_start_pos = (
            self.body.position[0] + size[0] / 2,
            self.body.position[1]
        )

        self.turret_end_pos = (
            sin(rad(self.direction)) * self.turret_size +
            self.turret_start_pos[0],
            cos(rad(self.direction)) *
            self.turret_size + self.turret_start_pos[1]
        )

        self.fire_timer += 1

    def render(self, window):
        # Render Body
        pygame.draw.rect(window, self.color, self.rect)

        # Render Turret
        pos = self.body.position
        size = self.vertices[2]
        pygame.draw.line(window, (100, 100, 100), self.turret_start_pos,
                         self.turret_end_pos, ceil(size[0] * 0.2))

        # Render Stats
        angle_pos = (pos[0] + size[0]/2, pos[1] + size[1]*2)
        text(window, str(int(self.direction)) + "˚", 25, (255, 255, 255), angle_pos)

        power_pos = (angle_pos[0], angle_pos[1] + size[1] * 2)
        text(window, str(int(self.fire_power)), 25, (255, 255, 255), power_pos)
