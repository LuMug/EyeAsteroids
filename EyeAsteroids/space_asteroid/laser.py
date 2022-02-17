import pygame
from utils import load_sprite
from game import Game
from pygame.math import Vector2


class Laser(Game):

	def __init__(self, position):
		super().__init__(
			position, load_sprite("laser"), Vector2(0)
		)

	def rotation(self):
		pass

	def length(self):
		pass