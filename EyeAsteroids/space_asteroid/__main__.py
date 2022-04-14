from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from startgame import EyeAsteroids
import pygame
import sys

if __name__ == "__main__":
    try:
        eyeAsteroids = EyeAsteroids()
        print("Start Game")
        eyeAsteroids.main_loop()
    except:
        eyeAsteroids.cancel_wait()
        print("\r\nGame quit")
        quit()
