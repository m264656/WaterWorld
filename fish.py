#create a pygame sprite class for a fish

import pygame
import random

class Fish(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image = pygame.image.load("..assets/sprites/purple_fish.png").convert()
        self.image.set_colorkey((0,0,0))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = 3
        self.rect.center = (x,y)

    def update(self):
        #update y position of fish
        self.y -= self.speed
        self.rect.y = self.y

    def draw(self, surf):
        surf.blit(self.image, self.rect)

fishes = pygame.sprite.Group()