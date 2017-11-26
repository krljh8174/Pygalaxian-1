from arms import *
import os
import pygame
import sys
import time
import math
import random
from pygame.locals import *
from unit import load_image


class bullet(arms):

    def __init__(
        self,
        x,
        y,
        color,
        direction=1,
        ):

        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image,self.rect = load_image('lazer.png',5,25,-1)
        self.rect.center = (x, y - direction * 20)
        self.direction = direction

    def update(self):
        (x, y) = self.rect.center
        y -= self.direction * 20
        self.rect.center = (x, y)
        if y <= 0 or y >= height:
            self.kill()
