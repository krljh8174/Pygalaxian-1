from unit import *
import os
import pygame
import sys
import time
import math
import random
from pygame.locals import *

class enemystation(unit):

    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self, self.containers)
        (self.image, self.rect) = load_image('spacestation_scale.png',
                150, 150, -1)

        self.rect.center = (x, -self.rect.height)
        self.health = 60
        self.waitTime = 0
        self.fire = 1
        self.movement = [0, 0]
        self.shot = False
        self.explosion_sound = \
            pygame.mixer.Sound('Sprites/explosion.wav')
        self.explosion_sound.set_volume(0.1)
        self.rotation = 10

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
            explosion(x, y,150)
            self.kill()

        if self.waitTime > 0:
            self.image = pygame.transform.rotate(self.image, 90)

    def drawplayer(self):
        screen.blit(self.image, self.rect)

    def shoot(self):
        (x, y) = self.rect.center
        for j in range(-12, 12):
            self.shot = enemybullet(x, y, (0, 255, 0), [j / 3.0, 1], 10)
        if self.waitTime % 2 == 1:
            enemy(random.randrange(0, 4))

        if self.waitTime % 12 == 1:
            enemysaucer(random.randrange(0, width - 50))

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
