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
from database import *


class EyeAsteroids:

    
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((1500, 900))
        #self.background = load_sprite("home", False)
        self.clock = pygame.time.Clock()
        createDatabase()
        
        # font = pygame.font.Font('./assets/font/SFFunkOblique.ttf', 50)

        # stato del gioco: 0 -> home; 1 -> gioco; 2 -> info gioco; 3 -> fine gioco
        self.state_game = 0;

        # attributo per calcolare la durata tra laser e asteroide
        self.last_time = None

        #Oggetti del gioco
        self.x, self.y = pygame.display.get_surface().get_size()
        self.spaceship = None
        self.asteroids = []
        

        # Genera gli asteroidi in modo casuale nella superficie
        self.wait = 0
        self.cancel_wait = self._wait_for_spawn(6)

        #punteggio
        self.points = 0

        self.player = ""


    def _wait_for_spawn(self, interval):
        stopped = Event()
        def loop():
            print("a")
            while not stopped.wait(self.wait):
                if self.state_game == 1 or self.state_game == 0:
                    self.wait = random.randint(2, 5)
                    self._spawn_asteroids(self.wait * 2)
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
                self.spaceship = Spaceship((self.x/2, self.y/2))
                self.laser = Laser((self.x/2, self.y/2))
                self._process_game_logic()
                self._draw_game()

            elif self.state_game == 2:
                self._draw_info()
            elif self.state_game == 3:
                self._draw_insert_name()
            else:
                self._draw_end()


    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("EyeAsteroids")

    def _draw_home(self):
        self.screen.fill((0,0,0))
        for asteroid in self.asteroids:
            asteroid.move()
            asteroid.draw(self.screen)


        self.title = writeText("EyeAsteroids",self.x / 2,100,60,(255,255,255),self)
        self.button = writeText("Press ENTER to start",self.x / 2,300,40,(255,255,255),self)
        self.info = writeText("Press [i] for info",self.x - 125,self.y - 20,25,(255,255,255),self)
        pygame.display.flip()

    def _draw_game(self):

        self.screen.fill((0,0,0))
        self.wirte = writeText("Score: " + str(self.points),self.x / 2,10,20,(255,255,255),self)
        for game_object in self._get_game_objects():
            game_object.draw(self.screen)

        self._laser_collision()
        pygame.display.flip()


    def _draw_info(self):
        self.screen.fill((0,0,0))
        pygame.draw.rect(self.screen,(255,255,255),(300,270,200,60))
        self.wirte = writeText("Info",self.x / 2,100,60,(255,255,255),self)
        self.wirte = writeText("...",self.x / 2,300,40,(0,0,0),self)
        pygame.display.flip()


    def _draw_insert_name(self):
        self.screen.fill((0,0,0))
        self.wirte = writeText("Game Over",self.x / 2,100,60,(255,255,255),self)
        self.wirte = writeText("Type your name:",self.x / 2,350,30,(255,255,255),self) 
        self.wirte = writeText(self.player+"_",self.x / 2,400,30,(255,255,255),self) 
        pygame.display.flip()

    def _draw_end(self):
        self.screen.fill((0,0,0))
        #pygame.draw.rect(self.screen,(255,255,255),(50,200,self.x - 100,350))
        self.wirte = writeText("Game Over",self.x / 2,100,60,(255,255,255),self)
        self.wirte = writeText("Ranking:",self.x / 2,225,30,(255,255,255),self)
        rows = showResult()
        
        pos_y = 300
        place = 1
        for row in rows:
            self.wirte = writeText(f"{place}. {row[0]}   {row[1]}",self.x / 2,pos_y,30,(255,255,255),self)
            pos_y += 50
            place += 1
        self.wirte = writeText("Press H to back home",self.x / 2,150,20,(255,255,255),self)
        self.wirte = writeText(f"Your Rank: {self.points}",self.x / 2,self.y - 50,30,(255,255,255),self)
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
                self.points += asteroid.point
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
        angle = 0
        for _ in range(spawn_x):
            random_x = random.randrange(1,10)
            if random_x <= 5:
                x = 0 - 120
                angle = random.randint(285,435)
            else:
                x = self.x + 120
                angle = random.randint(105,255)
            pos = Vector2(
                x,
                random.randrange(self.y)
            )
            self.asteroids.append(Asteroid(pos, angle))
        for _ in range(spawn_y):
            random_y = random.randint(1, 10)
            if random_y <= 5:
                y = 0 - 120
                angle = random.randrange(15,165)
            else:
                y = self.y + 120
                angle = random.randint(195,345)
            pos = Vector2(random.randrange(self.x),y)
            self.asteroids.append(Asteroid(pos, angle))
    
    
    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.cancel_wait()
                quit()
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) and self.state_game == 0:
                self.asteroids = []
                self.state_game = 1
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_i) and self.state_game == 0:
                self.state_game = 2
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_i) and self.state_game == 2:
                self.state_game = 0
            elif (self.state_game == 3):

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        insertResult(self.points, self.player)
                        if len(self.player) > 0 :
                            self.player = ''
                            self.state_game = 4
                    elif event.key == pygame.K_BACKSPACE:
                        self.player = self.player[:-1]
                    else:
                        self.player += event.unicode
            elif (event.type == pygame.KEYDOWN and (event.key == pygame.K_r or event.key == pygame.K_h)) and self.state_game == 4:
                eyeAsteroids = EyeAsteroids()
                eyeAsteroids.main_loop()
                del self

                self.state_game = 1
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_h) and self.state_game == 4:
                self.state_game = 0