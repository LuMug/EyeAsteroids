import pygame
from utils import load_sprite
from utils import writeText
from asteroid import Asteroid


class EyeAsteroids:
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("background", False)
        self.clock = pygame.time.Clock()
        # font = pygame.font.Font('./assets/font/SFFunkOblique.ttf', 50)

        # stato del gioco: 0 -> home; 1 -> gioco; 2 -> fine gioco
        self.state_game = 0;
        self.asteroid = Asteroid((200,200))

    def main_loop(self):
        while True:
            self._handle_input()

            if self.state_game == 0:
                self._draw_home()
            elif self.state_game == 1:
                self._draw_game()

            elif self.state_game == 2:
                self._draw_info()
            else:
                self._draw_end()


    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("EyeAsteroids")

    def _draw_home(self):
        self.screen.blit(self.background, (0, 0))
        pygame.draw.rect(self.screen,(255,255,255),(300,270,200,60))
        self.wirte = writeText("EyeAsteroids",400,100,60,(255,255,255),self)
        self.wirte = writeText("START",400,300,40,(0,0,0),self)
        pygame.display.flip()
        self.clock.tick(60)

    def _draw_game(self):
        self.screen.fill((0,0,0))
        
        self._process_game_logic()
        pygame.display.flip()
        #self.wirte.kill()
        #self.screen.blit(self.background, (0, 0))
        #pygame.draw.rect(self.screen,(255,255,255),(300,270,200,60))
        #self.wirte = writeText("EyeAsteroids",400,100,60,(255,255,255),self)
        #self.wirte = writeText("START",400,300,40,(0,0,0),self)
        #pygame.display.flip()
        #self.clock.tick(60)
        



    def _draw_info(self):
        self.screen.fill((0,0,0))
        pygame.draw.rect(self.screen,(255,255,255),(300,270,200,60))
        self.wirte = writeText("Informazioni",400,100,60,(255,255,255),self)
        self.wirte = writeText("...",400,300,40,(0,0,0),self)
        pygame.display.flip()
        self.clock.tick(60)


    def _draw_end(self):
        pass

    def _process_game_logic(self):
        self._get_game_objects().draw(self.screen)


    def _get_game_objects(self):
        return self.asteroid
    
 	
    def _handle_input(self):
    	for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            	quit()
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) and self.state_game == 0:
                self.state_game = 1
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_i) and self.state_game == 0:
                self.state_game = 2
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_i) and self.state_game == 2:
                self.state_game = 0