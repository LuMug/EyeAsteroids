from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from startgame import Startgame
import pygame
import sys

if __name__ == "__main__":
    try:
        eyeAsteroids = Startgame()
        print("Start Game")
        eyeAsteroids.main_loop()
    except:
        eyeAsteroids.cancel_wait()
        print("\r\nGame quit")
        quit()
