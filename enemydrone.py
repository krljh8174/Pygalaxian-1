from unit import *
import os
import pygame
import sys
import time
import math
import random
from pygame.locals import *
from explosion import *
from enemybullet import *


class enemydrone(unit):

    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self, self.containers)
        (self.image, self.rect) = load_image('enemy2_scale.png', 50,
                102, -1)
        self.rect.top = -self.rect.height
        self.rect.left = x

        self.speed = 0
        self.fire = 1
        self.movement = [0, 0]
        self.health = 20

        self.shot = False
        self.waitTime = 0
        self.explosion_sound = \
            pygame.mixer.Sound('Sprites/explosion.wav')
        self.explosion_sound.set_volume(0.1)

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
        self.autopilot()
        self.rect = self.rect.move(self.movement)

        if self.fire == 1 and self.waitTime % 10 == 1:
            self.shoot()

        if self.health <= 0:
            (x, y) = self.rect.center
            if pygame.mixer.get_init():
                self.explosion_sound.play(maxtime=1000)
            explosion(x, y,100)
            self.kill()

    def drawplayer(self):
        screen.blit(self.image, self.rect)

    def shoot(self):
        (x, y) = self.rect.center
        self.shot = enemybullet(x, y + self.rect.height / 2, (255, 0,
                                0), [0, 1], 10)
        self.shot = enemybullet(x, y + self.rect.height / 2, (255, 0,
                                0), [-0.5, 1], 10)
        self.shot = enemybullet(x, y + self.rect.height / 2, (255, 0,
                                0), [0.5, 1], 10)
        self.shot = enemybullet(x, y + self.rect.height / 2, (255, 0,
                                0), [-1, 1], 10)
        self.shot = enemybullet(x, y + self.rect.height / 2, (255, 0,
                                0), [1, 1], 10)

    def autopilot(self):
        if self.rect.top < height - 500:
            self.movement[1] = 3
        elif self.rect.top > height - 500 and self.waitTime < 1000:
            self.movement[1] = 0
            self.waitTime += 1

        if self.waitTime >= 150:
            self.movement[1] = 5

        if self.rect.top > height:
            self.kill()
