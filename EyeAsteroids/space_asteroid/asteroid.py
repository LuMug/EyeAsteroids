import pygame
from utils import load_sprite
from game import Game
import random
from pygame.math import Vector2
class Asteroid(Game):

	def __init__(self, position):
		random_sprite = [
							["asteroid0",100],
							["asteroid1",50],
							["asteroid2",20]
						]
		sprite_name = random_sprite[random.randint(0, 2)][0];
		super().__init__(
			position, load_sprite(sprite_name), self.random_velocity()
		)


	def random_velocity(self):
		speed = random.randint(1, 2)
		return Vector2(speed, 0).rotate(random.randrange(360))