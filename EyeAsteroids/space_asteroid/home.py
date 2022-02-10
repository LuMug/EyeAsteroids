import pygame
from utils import load_sprite
from utils import writeText



class Home:
	
	def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("background", False)
        clock = pygame.time.Clock()
        #font = pygame.font.Font('./assets/font/SFFunkOblique.ttf', 50)