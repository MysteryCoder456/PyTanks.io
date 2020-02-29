import pygame
import pymunk


class Bullet:
    """Class for making a bullet

    Arguments:
        pos {tuple} -- Starting position of the bullet.
        vel {tuple} -- Starting velocity of the bullet.
        radius {int} -- Radius of bullet (to make relative to tank size).
    """

    def __init__(self, pos, vel, radius):
        mass = radius * 0.4
        offset = (-radius/2, -radius/2)

        self.body = pymunk.Body(mass)
        self.body.moment = pymunk.moment_for_circle(
            mass, 0, radius, offset=offset
        )
        self.body.center_of_gravity = offset

        self.body.position = pos
        self.body.velocity = vel

        self.shape = pymunk.Circle(self.body, radius, offset=offset)

        self.alive_time = 0
        self.color = (150, 150, 150)
        self.update()

    def update(self):
        pos = self.body.position
        radius = self.shape.radius
        self.rect = pygame.Rect(pos[0] - radius, pos[1] - radius, radius * 2, radius * 2)
        self.alive_time += 1

    def add_to_space(self, space):
        space.add(self.body, self.shape)

    def render(self, window):
        pygame.draw.ellipse(window, self.color, self.rect)
