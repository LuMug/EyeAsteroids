import pygame
from utils import load_sprite
from game import Game
import random
from pygame.math import Vector2
class Asteroid(Game):

	MIN_DISTANCE = 200;

	def __init__(self, spaceship):
		super().__init__(
			self.random_position(spaceship), load_sprite("asteroid1"), self.random_velocity()
		)



	def random_position(self, spaceship):

		#x, y = pygame.display.get_surface().get_size()
		#andom_x = random.randint(0, x)
		#random_y = random.randint(0, y)
		#if random_x > x - x/2 - self.MIN_DISTANCE and random_x < x - x/2 + self.MIN_DISTANCE:
		#	if x >= x/2:
		#		random_x = x/2 + self.MIN_DISTANCE
		#	else:
		#		random_x = x/2 - self.MIN_DISTANCE

		#if random_y > y - y/2 - self.MIN_DISTANCE and random_y < y - y/2 + self.MIN_DISTANCE:
		#	if y >= y/2:
		#		random_y = y/2 + self.MIN_DISTANCE
		#	else:
		#		random_y = y/2 - self.MIN_DISTANCE
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