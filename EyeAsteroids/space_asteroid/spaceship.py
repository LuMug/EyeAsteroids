import pygame
import random
from pygame.math import Vector2
from utils import load_sprite
from game import Game

class Spaceship(Game):
	

	def __init__(self, position):
		super().__init__(
			position, load_sprite("spaceship"), Vector2(0)
		)
