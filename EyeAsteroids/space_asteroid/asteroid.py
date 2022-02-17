import pygame
from utils import load_sprite
from game import Game
import random
from pygame.math import Vector2
class Asteroid(Game):

	def __init__(self, position):
		super().__init__(
			position, load_sprite("asteroid1"), self.random_velocity()
		)



	def random_position(self, spaceship):
		position = Vector2(
				random.randrange(pygame.display.get_surface().get_width()),
				random.randrange(pygame.display.get_surface().get_height()),
			)
		while True:
			if position.distance_to(spaceship.position) > self.MIN_DISTANCE:
				break

		return position


	def random_velocity(self):
		speed = random.randint(20, 60)
		return Vector2(speed)