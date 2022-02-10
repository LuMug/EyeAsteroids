import pygame
from utils import load_sprite
from utils import writeText


class EyeAsteroids:
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("background", False)
        clock = pygame.time.Clock()
        #font = pygame.font.Font('./assets/font/SFFunkOblique.ttf', 50)

    def main_loop(self):
        while True:
            self._handle_input()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("EyeAsteroids")


    def _draw(self):
        self.screen.blit(self.background, (0, 0))
        pygame.draw.rect(self.screen,(255,255,255),(300,270,200,60))
        self.wirte = writeText("EyeAsteroids",400,100,60,(255,255,255),self)
        self.wirte = writeText("START",400,300,40,(0,0,0),self)
        pygame.display.flip()

	
    def _handle_input(self):
    	for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            	quit()