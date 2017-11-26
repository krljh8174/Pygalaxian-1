from unit import unit
from unit import load_image
import os
import pygame
import sys
sys.path.append("C:\\Users\\zidru\\Desktop\\PyGalaxian-master\\bullets")
import time
import math
import random
from bullet import bullet
from pygame.locals import *
size = (width, height) = (1024, 768)
screen = pygame.display.set_mode(size,DOUBLEBUF | FULLSCREEN)

class player(unit):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        (self.image, self.rect) = load_image('fighter1_scale.png', 72,
                72, -1)
        self.rect.top = size[1] - 100#500
        self.rect.left = size[0]/2#200

        self.speed = 0
        self.fire = 0
        self.movement = [0, 0]
        self.trigger = 0
        self.health = 200
        self.kills = 0
        self.score = 0
        self.shootdelay = 0
        self.isautopilot = False
        self.shot = False
        self.won = False

    def checkbounds(self):
        if self.rect.left < 0:
            self.rect.left = 0
            self.movement[0] = 0
            self.speed = 0
        if self.rect.right > width:
            self.rect.right = width
            self.movement[0] = 0
            self.speed = 0

    def update(self):
        self.rect = self.rect.move(self.movement)
        self.shootdelay += 1
        if self.fire == 1 and self.shootdelay%3 == 1:
            self.shoot()

        if self.health > 200:
            self.health = 200

    def drawplayer(self):
        screen.blit(self.image, self.rect)

    def shoot(self):
        (x, y) = self.rect.center
        self.shot = bullet(x - 14, y, (0, 255, 0), 1)
        self.shot = bullet(x + 14, y, (0, 255, 0), 1)

    def autopilot(self):
        if self.rect.centerx < width / 2:
            self.movement[0] = 5
        else:
            self.movement[0] = -5
        if self.rect.centerx - width / 2 < 5 and self.rect.centerx \
            - width / 2 > -5:
            self.movement[0] = 0
            self.movement[1] = -10
