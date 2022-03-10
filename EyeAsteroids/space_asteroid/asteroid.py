import pygame
from utils import load_sprite
from game import Game
import random
from pygame.math import Vector2


class Asteroid(Game):

	def __init__(self, position, angle):
		random_sprite = [
							["asteroid0",100,250,4],
							["asteroid1",50,500,2],
							["asteroid2",20,750,1]
						]
		rand = random.randint(0, 2)
		self.sprite_name = random_sprite[rand][0]
		self.point = random_sprite[rand][1]
		# attributo per definire quanti secondi servono per distruggere l'asteroide
		self.life = random_sprite[rand][2]
		self.speed = random_sprite[rand][3]
		super().__init__(
			position, load_sprite(self.sprite_name), Vector2(self.speed, 0).rotate(angle)
		)
