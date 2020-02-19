# CLASS IMPORTS
from ground import Ground

import pygame
pygame.init()


class PyTanksIO:
    def __init__(self, width, height, title):
        # Window initializing code
        self.width = width
        self.height = height
        self.win = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        self.clock = pygame.time.Clock()
        self.running = True
        self.FPS = 60
        self.background = (0, 0, 0)

    def start(self):
        # Game initializing code
        self.ground = Ground(self.width, self.height)

    def logic(self):
        pass

    def render(self):
        self.win.fill(self.background)

        self.ground.render(self.win)

        pygame.display.update()


def main():
    game = PyTanksIO(1024, 700, "PyTanks.io")
    game.start()

    while game.running:
        game.clock.tick(game.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False

        game.logic()
        game.render()


if __name__ == "__main__":
    main()
    pygame.quit()
    quit()
