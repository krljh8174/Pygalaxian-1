import os
import pygame
import sys
import time
import math
import random
from pygame.locals import *

size = (width, height) = (1024, 768)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 155, 0)
red = (155, 0, 0)
sky = (0, 0, 0)
clock = pygame.time.Clock()
FPS = 21
maxspeed = 15
screen = pygame.display.set_mode(size,DOUBLEBUF | FULLSCREEN)

class unit(pygame.sprite.Sprite):
    def __init__(self):
        pass
    def checkbounds(self):
        pass
    def update(self):
        pass
    def drawplayer(self):
        pass
    def shoot(self):
        pass

        

def load_image(
    name,
    sizex=-1,
    sizey=-1,
    colorkey=None,
    ):

    fullname = os.path.join('Sprites', name)
    image = pygame.image.load(fullname)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)

    if sizex != -1 or sizey != -1:
        image = pygame.transform.scale(image, (sizex, sizey))

    return (image, image.get_rect())
