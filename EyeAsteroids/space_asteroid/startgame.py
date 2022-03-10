import pygame
import random
from threading import Event, Thread
from pygame.math import Vector2
from utils import load_sprite
from utils import writeText
from utils import point_in_object
from asteroid import Asteroid
from spaceship import Spaceship
from laser import Laser


class EyeAsteroids:

    
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("background", False)
        self.clock = pygame.time.Clock()
        
        # font = pygame.font.Font('./assets/font/SFFunkOblique.ttf', 50)

        # stato del gioco: 0 -> home; 1 -> gioco; 2 -> info gioco; 3 -> fine gioco
        self.state_game = 0;

        # attributo per calcolare la durata tra laser e asteroide
        self.last_time = None

        #Oggetti del gioco
        self.x, self.y = pygame.display.get_surface().get_size()
        self.spaceship = Spaceship((self.x/2, self.y/2))
        self.asteroids = []
        self.laser = Laser((self.x/2, self.y/2))

        # Genera gli asteroidi in modo casuale nella superficie
        self.wait = 0
        self.cancel_wait = self._wait_for_spawn(5)

        #punteggio
        self.points = 0



    def _wait_for_spawn(self, interval):
        stopped = Event()
        def loop():
            while not stopped.wait(self.wait):
                if self.state_game == 1:
                    self._spawn_asteroids(10)
                    if self.wait == 0:
                        self.wait = interval

        Thread(target=loop).start()    
        return stopped.set

        

    def main_loop(self):
        while True:
            self.clock.tick(60)
            self._handle_input()

            if self.state_game == 0:
                self._draw_home()

            elif self.state_game == 1:
                self._process_game_logic()
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
        self.title = writeText("EyeAsteroids",400,100,60,(255,255,255),self)
        self.button = writeText("START",400,300,40,(0,0,0),self)
        pygame.display.flip()

    def _draw_game(self):

        self.screen.fill((0,0,0))
        self.wirte = writeText("Punteggio: " + str(self.points),400,10,20,(255,255,255),self)
        for game_object in self._get_game_objects():
            game_object.draw(self.screen)

        self._laser_collision()
        pygame.display.flip()


    def _draw_info(self):
        self.screen.fill((0,0,0))
        pygame.draw.rect(self.screen,(255,255,255),(300,270,200,60))
        self.wirte = writeText("Informazioni",400,100,60,(255,255,255),self)
        self.wirte = writeText("...",400,300,40,(0,0,0),self)
        pygame.display.flip()


    def _draw_end(self):
        self.screen.fill((0,0,0))
        pygame.draw.rect(self.screen,(255,255,255),(300,270,200,60))
        self.wirte = writeText("Game Over",400,100,60,(255,255,255),self)
        self.wirte = writeText("Classifica:",400,300,30,(0,0,0),self)
        pygame.display.flip()


    def _process_game_logic(self):
        for game_object in self._get_game_objects():
            game_object.move()


        #collisione degli asteroidi con la navicella
        if self.spaceship:
            for asteroid in self.asteroids:
                if asteroid.collides_with(self.spaceship):
                    self.state_game = 3
                    self.cancel_wait()


    def _get_game_objects(self):
        return [*self.asteroids, self.spaceship]


    def _laser_collision(self):
        
        asteroid = self._collide_any_asteroid()
        if(asteroid != None):  
            self.laser.draw(self.screen)

            if self.last_time == None:
                self.last_time = pygame.time.get_ticks()
            
            now = pygame.time.get_ticks()
            delta = now - self.last_time;
            asteroid.life -= delta
            self.last_time = now
            if asteroid.life <= 0: 
                self.asteroids.remove(asteroid)
                del asteroid
        else:
            self.last_time = None
                      
    def _collide_any_asteroid(self):
        for asteroid in self.asteroids:
            if(point_in_object(pygame.mouse.get_pos(),asteroid)):
                return asteroid;
        return None;


    def _spawn_asteroids(self, quantity):
        spawn_x = random.randrange(0, quantity)
        spawn_y = quantity - spawn_x
        for _ in range(spawn_x):
            random_x = random.randrange(1,10)
            if random_x <= 5:
                x = 0 - 120
            else:
                x = self.x + 120
            pos = Vector2(
                x,
                random.randrange(self.y)
            )
            self.asteroids.append(Asteroid(pos))
        for _ in range(spawn_y):
            random_y = random.randrange(1, 10)
            if random_y <= 5:
                y = 0 - 120
            else:
                y = self.y + 120
            pos = Vector2(random.randrange(self.x),y)
            self.asteroids.append(Asteroid(pos))
    
 	
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
            # bottone start all'inizio del gioco
            #elif event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pressed()[0] and :


    #for _ in range(spawn_y):
            #while True:
                #pos = Vector2(
                        #random.randrange(self.x),
                        #random.randrange(self.y)
                    #)
                #if(pos.distance_to(self.spaceship.position)> self.MIN_DISTANCE):
                    #break
            #self.asteroids.append(Asteroid(pos))

