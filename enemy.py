import pygame
import time as t
from random import randint
from base import Entity

screen = pygame.display.set_mode((1280, 720))


class Enemy(Entity):
    """Enemy class. Needs Y Coordinate & Image."""

    def __init__(self, y, *image):
        Entity.__init__(self)
        self.image = image[0]
        self.rect = self.image.get_rect()
        self.pos_x = 1300
        self.pos_y = y
        self.speed = self.generate(4, 8)

    def draw(self):
        screen.blit(self.image, (self.pos_x, self.pos_y))

    def generate(self, n1, n2):
        randomnumber = randint(n1, n2)
        return randomnumber

    def update(self):
        self.draw()
        self.move(self.speed)

    def move(self, speed):
        self.pos_x -= speed
        if self.pos_x < -50:
            self.pos_x = 1300
            self.speed = self.generate(4, 8)
