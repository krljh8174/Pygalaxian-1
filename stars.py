import os
import pygame
import sys
import time
import math
import random
from pygame.locals import *

size = (width, height) = (1024, 768)
screen = pygame.display.set_mode(size,DOUBLEBUF | FULLSCREEN)


class stars:

    
    def __init__(self,radius,color,nofstars,speed=5):
        self.radius = radius
        self.color = color
        self.speed = speed
        self.nofstars = nofstars
        self.starpos = [[0 for j in range(2)] for i in range(self.nofstars)]
        for x in range(self.nofstars):
            self.starpos[x][0] = random.randrange(0, width)
            self.starpos[x][1] = random.randrange(0, height)

    def drawstars(self):
        for x in range(self.nofstars):
            #pygame.draw.rect(screen, color, [self.starpos[x][0],
            #                 self.starpos[x][1], 2, 2])
            pygame.draw.circle(screen,self.color,(self.starpos[x][0],self.starpos[x][1]),self.radius)
        self.movestars()

    def movestars(self):
        
        for x in range(self.nofstars):
            self.starpos[x][1] += self.speed
            if self.starpos[x][1] > height:
                self.starpos[x][1] = 0
