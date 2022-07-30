import pygame
from pygame.sprite import Sprite

class Star(Sprite):
	"""A class to represent a single star in the grid"""

	def __init__(self, grid_star):
		"""Initialize the star and set its starting position"""
		super().__init__()
		self.screen = grid_star.screen

		# Load the star and set its rect attribute.
		self.image = pygame.image.load('star.bmp')
		self.rect = self.image.get_rect()

		# Start each new star near the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = 0 #self.rect.height

		# Store the star's exact horizontal position.
		self.x = float(self.rect.x)