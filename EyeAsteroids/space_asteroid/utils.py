import pygame
from pygame.image import load

def load_sprite(name, with_alpha=True):
    path = f"./assets/sprites/{name}.png"
    loaded_sprite = load(path)

    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()

def writeText(string, coordx, coordy, fontSize,color, self):
    font = pygame.font.Font('./assets/font/SFFunkOblique.ttf', fontSize)
    text = font.render(string, True, color)
    textRect = text.get_rect()
    textRect.center = (coordx, coordy)
    self.screen.blit(text, textRect)

def point_in_object(point, obj):    
    distance = obj.position.distance_to(point)
    return distance < obj.radius
