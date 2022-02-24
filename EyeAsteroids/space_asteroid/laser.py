import pygame
from utils import load_sprite
from game import Game
from pygame.math import Vector2


class Laser(Game):

	def __init__(self, position):
		super().__init__(
			position, load_sprite("laser"), Vector2(0)
		)

	# disegna la linea, ricevendo la coordinata (x,y)
	def draw(self, surface, coordinate):
		w,h = surface.get_size()

		# disegna la linea dal centro alla coordinata indicata
		pygame.draw.line(surface, (255,255,255), (w/2, h/2), coordinate)

	