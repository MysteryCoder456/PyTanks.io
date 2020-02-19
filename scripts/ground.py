import pygame


class Ground:
    def __init__(self, window_width, window_height):
        self.x = 0
        self.y = window_height - 150

        self.width = window_width
        self.height = window_height - self.y
        self.color = (0, 170, 0)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def render(self, window):
        pygame.draw.rect(window, self.color, self.rect)

    def collide(self, Rect):
        return self.rect.colliderect(Rect)
