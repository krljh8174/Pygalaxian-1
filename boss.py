from unit import *
import os
import pygame
import sys
import time
import math
import random
from pygame.locals import *
from enemy import *
from enemybullet import *
from enemydrone import *
from enemysaucer import *


class boss(unit):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        (self.image, self.rect) = load_image('boss.png', 200, 400, -1)#125, 250, -1)
        self.rect = self.image.get_rect()
        self.rect.top = 100
        self.rect.left = random.randrange(0, width - 72)

        self.speed = 0
        self.fire = 0
        self.movement = [0, 0]
        self.trigger = 0
        self.health = 600
        self.bulletformation = 0
        self.bulletspeed = 20
        self.spreecount = 0
        self.spree = False
        self.shot = False
        self.isautopilot = False
        self.reloadtime = 0

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

        self.rect = self.rect.move(self.movement)

        if self.fire == 1 and self.reloadtime == 0:
            self.shoot(self.bulletformation, self.bulletspeed)

        if self.reloadtime > 0:
            self.reloadtime -= 1

        if self.health <= 0:
            self.kill()

        if self.spree == True and self.spreecount <= 70:
            self.spreecount += 1
            if self.spreecount % 5 == 1:
                self.movement[0] = 0
                self.speed = 0
                self.shoot(1, 10)
            else:
                pass
        else:
            self.spree = False
            self.spreecount = 0

    def drawplayer(self):
        screen.blit(self.image, self.rect)

    def shoot(self, bulletformation=0, bulletspeed=20):
        (x, y) = self.rect.center
        if bulletformation == 0:
            self.shot = enemybullet(x, y + self.rect.height / 2, (255,
                                    0, 255), [0, 1], bulletspeed)
            self.shot = enemybullet(x - self.rect.width / 2 + 30, y
                                    - self.rect.height / 2 + 50, (255,
                                    0, 255), [0, 1], bulletspeed)
            self.shot = enemybullet(x + self.rect.width / 2 - 30, y
                                    - self.rect.height / 2 + 50, (255,
                                    0, 255), [0, 1], bulletspeed)
        elif bulletformation == 1:
            self.shot = enemybullet(x, y, (255, 0, 255), [1.5, 1],
                                    bulletspeed)
            self.shot = enemybullet(x, y, (255, 0, 255), [-1.5, 1],
                                    bulletspeed)
            self.shot = enemybullet(x, y, (255, 0, 255), [1.2, 1],
                                    bulletspeed)
            self.shot = enemybullet(x, y, (255, 0, 255), [-1.2, 1],
                                    bulletspeed)
            self.shot = enemybullet(x, y, (255, 0, 255), [0, 1],
                                    bulletspeed)
            self.shot = enemybullet(x, y, (255, 0, 255), [0.9, 1],
                                    bulletspeed)
            self.shot = enemybullet(x, y, (255, 0, 255), [-0.9, 1],
                                    bulletspeed)
            self.shot = enemybullet(x, y, (255, 0, 255), [0.6, 1],
                                    bulletspeed)
            self.shot = enemybullet(x, y, (255, 0, 255), [-0.6, 1],
                                    bulletspeed)
            self.shot = enemybullet(x, y, (255, 0, 255), [0.3, 1],
                                    bulletspeed)
            self.shot = enemybullet(x, y, (255, 0, 255), [-0.3, 1],
                                    bulletspeed)

        if random.randrange(0, 10) == 4:
            enemy(random.randrange(0, 4))
        if random.randrange(0, 50) == 41:
            enemysaucer(random.randrange(0, width - 50))
        if random.randrange(0, 200) == 121:
            enemydrone(random.randrange(0, width - 50))

