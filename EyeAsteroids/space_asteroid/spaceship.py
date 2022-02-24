import pygame
from pygame.math import Vector2
from pygame.transform import rotozoom
from utils import load_sprite
from game import Game
from math import atan2, pi



class Spaceship(Game):
	

	def __init__(self, position):
		super().__init__(
			position, load_sprite("spaceship"), Vector2(0)
		)

	# disegna la navicella e ruota in base alle coordinate del giocatore che osserva lo schermo
	def draw(self, surface):
		position_spaceship_x, position_spaceship_y = self.position
		coordinate_x, coordinate_y = pygame.mouse.get_pos()

		angle = atan2(
				position_spaceship_y - coordinate_y,
				coordinate_x - position_spaceship_x
			) * 180 / pi
		
		#ruota l'immagine
		rotated_surface = rotozoom(self.sprite, angle, 1.0)

		#coordinate dell'immagine ruotato
		blit_position = self.position - (Vector2(rotated_surface.get_size())/2)
		surface.blit(rotated_surface, blit_position)