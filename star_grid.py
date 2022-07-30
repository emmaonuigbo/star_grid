import sys

import pygame

from star_grid_settings import Settings
from star import Star

class StarGrid():
	"""Overall class to manage the grid and behavior"""

	def __init__(self):
		"""Initialize the grid and its resources"""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode(
						(self.settings.screen_width, self.settings.screen_height))
		#self.settings.screen_width = self.screen.get_rect().width
		#self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("A Star Grid")

		self.star = Star(self)
		self.stars = pygame.sprite.Group()

	def run_grid(self):
		"""Start the main loop for the grid"""
		# Create an alien and place in the row
		while True:
			self._check_events()
			self._create_grid()
			self._update_screen()

	def _check_events(self):
		"""Respond to keypresses and mouse events"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

	def _create_grid(self):
		"""Create the grid of stars"""
		# Create a star and find the number of stars in a row
		star = Star(self)
		star_width, star_height = star.rect.width, star.rect.height
		available_space_x = self.settings.screen_width - star_width
		number_stars_x = available_space_x // star_width

		# Determine the number of rows of stars that fit on the screen.
		available_space_y = self.settings.screen_height
		number_rows = available_space_y // star_height

		# Create the full grid of stars
		for row_number in range(number_rows):
			for star_number in range(number_stars_x):
				self._create_star(star_number, row_number)

	def _create_star(self, star_number, row_number):
		"""Create a star and place it in the row"""
		star = Star(self)
		star_width, star_height = star.rect.size
		star.x = star_width + star_width * star_number
		star.rect.x = star.x
		star.rect.y = star.rect.height * row_number
		self.stars.add(star)

	def _update_screen(self):
		"""Update images to the screen and flip to the new screen."""
		self.screen.fill(self.settings.bg_color)
		self.stars.draw(self.screen)

		pygame.display.flip()

if __name__ == '__main__':
	# Make an instance of the grid and run it
	sg = StarGrid()
	sg.run_grid()