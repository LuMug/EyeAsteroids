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
		rand = random.randint(0, 2)
		self.sprite_name = random_sprite[rand][0]
		self.point = random_sprite[rand][1]
		super().__init__(
			position, load_sprite(self.sprite_name), self.random_velocity()
		)

		# attributo per definire quanti secondi servono per distruggere l'asteroide
		self.life = 500


	def random_velocity(self):
		speed = random.randint(1, 2)
		return Vector2(speed, 0).rotate(random.randrange(360))

