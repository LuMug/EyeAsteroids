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


	def random_velocity(self):
		speed = random.randint(1, 2)
		return Vector2(speed, 0).rotate(random.randrange(360))