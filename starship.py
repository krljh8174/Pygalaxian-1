from unit import *
import os
import pygame
import sys
import time
import math
import random
from pygame.locals import *
from enemy import moveplayer
from enemybullet import *
from explosion import *

# starship

class starship(pygame.sprite.Sprite):

    def __init__(self, n=0):
        pygame.sprite.Sprite.__init__(self, self.containers)
        sheet = pygame.image.load('Sprites/starship_scale.png')
        self.images = []

        rect = pygame.Rect((0, 0, 260, 174))
        image = pygame.Surface(rect.size)
        image.blit(sheet, (0, 0), rect)
        self.images.append(image)

        rect = pygame.Rect((0, 0, 260, 174))   
        image = pygame.Surface(rect.size)
        image.blit(sheet, (0, 0), rect)
        self.images.append(image)

        
        rect = pygame.Rect((0, 0, 260, 174))
        image = pygame.Surface(rect.size)
        image.blit(sheet, (0, 0), rect)
        self.images.append(image)

        
        rect = pygame.Rect((0, 0, 260, 174))
        image = pygame.Surface(rect.size)
        image.blit(sheet, (0, 0), rect)
        self.images.append(image)


        # (a,b,c,d) 는 (a,b) 부터 (c,d) 구간을 짜르라는 의미
        
        
        self.image = self.images[n]
        self.image = self.image.convert()
        colorkey = -1
        colorkey = self.image.get_at((10, 10))
        self.image.set_colorkey(colorkey, RLEACCEL)

        self.image = pygame.transform.scale(self.image, (36, 36))
        self.rect = self.image.get_rect()

        self.image = pygame.transform.rotate(self.image, 180)
        self.rect.top = 0
        self.rect.left = random.randrange(0, width - 1)

        self.speed = 0
        self.fire = 0
        self.movement = [0, 0]
        self.trigger = 0
        self.health = 2
        self.isautopilot = False

        self.explosion_sound = \
            pygame.mixer.Sound('Sprites/explosion.wav')
        self.explosion_sound.set_volume(0.1)

        self.shot = False

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
        self.checkbounds()

        moveplayer(self)
        self.autopilot()
        self.rect = self.rect.move(self.movement)

        if self.fire == 1:
            self.shoot()

        if self.health <= 0:
            (x, y) = self.rect.center
            if pygame.mixer.get_init():
                self.explosion_sound.play(maxtime=1000)
            explosion(x, y)
            self.kill()

    def drawplayer(self):
        screen.blit(self.image, self.rect)

    def shoot(self):
        (x, y) = self.rect.center
        self.shot = enemybullet(x, y, (255, 255, 0), [0, 1], 12)

    def autopilot(self):
        if self.rect.top < height:
            self.movement[1] = 5
        else:
            self.kill()
#  ~starship
