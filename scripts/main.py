import pygame
pygame.init()


class PygameTemplate:
	def __init__(self, width, height, title):
		self.width = width
		self.height = height
		self.win = pygame.display.set_mode((width, height))
		pygame.display.set_caption(title)

		self.clock = pygame.time.Clock()
		self.running = True
		self.FPS = 60
		self.background = (0, 0, 0)

	def start(self):
		pass

	def logic(self):
		pass

	def render(self, window):
		self.win.fill(self.background)

		pygame.display.update()
		
		
def main():
	game = PygameTemplate(1024, 720, "PygameTemplate")
	game.start()

	while game.running:
		game.clock.tick(game.FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game.running = False

		game.logic()
		game.render(game.win)
		
		
if __name__ == "__main__":
	main()
	pygame.quit()
	quit()
