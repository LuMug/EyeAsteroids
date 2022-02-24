import pygame
from pygame.math import Vector2
from pygame.transform import rotozoom
from utils import load_sprite
from game import Game



class Spaceship(Game):
	

	def __init__(self, position):
		super().__init__(
			position, load_sprite("spaceship"), Vector2(0)
		)

	def draw(self, surface):
		angle = 180
		
		#ruota l'immagine
		rotated_surface = rotozoom(self.sprite, angle, 1.0)

		#coordinate dell'immagine ruotato
		blit_position = self.position - (Vector2(rotated_surface.get_size())/2)
		surface.blit(rotated_surface, blit_position)