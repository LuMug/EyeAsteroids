import pygame
from utils import load_sprite
from game import Game
from pygame.math import Vector2


class Laser(Game):

	def __init__(self, start_point):
		self.start_point = start_point

	# disegna la linea, ricevendo la coordinata (x,y)
	def draw(self, surface):
		w,h = surface.get_size()
		
		coordinate = pygame.mouse.get_pos()


		# disegna la linea dal centro alla coordinata indicata
<<<<<<< HEAD
		pygame.draw.line(surface, (255,255,255), self.start_point, coordinate, width=2)
=======
		pygame.draw.line(surface, (255,255,255), self.start_point, coordinate, width=2)

>>>>>>> 12db091a2a8014f5fafda0add4d3e5be7d07e6e9