from unit import *
import os
import pygame
import sys
import time
import math
import random
from pygame.locals import *


class healthpack(unit):

    def __init__(
        self,
        x,
        y,
        health,
        ):

        pygame.sprite.Sprite.__init__(self, self.containers)
        self.health = health
        (self.image, self.rect) = load_image('healthpack.png', 40, 40,
                -1)
        self.rect.left = x
        self.rect.top = y
        self.movement = [3, 0]
        self.maxleft = self.rect.left - 20
        self.maxright = self.rect.right + 20

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

        if self.health <= 0 or self.rect.top > height:
            self.kill()

    def drawplayer(self):
        screen.blit(self.image, self.rect)

    def autopilot(self):
        if self.rect.right > self.maxright:
            self.movement[0] = -3
        elif self.rect.left < self.maxleft:
            self.movement[0] = 3

        self.movement[1] = 5
