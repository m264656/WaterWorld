import pygame
from parameters import *

class Fish(pygame.sprite.Sprite):

    def __init__(self, x, y, speed=player_speed):
        super().__init__()
        self.image = pygame.image.load("../assets/sprites/purple_fish.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = speed
        self.rect.center = (x,y)

    def increase_speed(self):
        if self.speed < MAX_SPEED:
            self.speed += 0.05

    def decrease_speed(self):
        if self.speed > MIN_SPEED:
            self.speed -= 0.05
        else:
            self.speed = MIN_SPEED

    def update(self):
        #update y position of fish
        self.y -= self.speed
        self.rect.y = self.y

    def draw(self, surf):
        surf.blit(self.image, self.rect)

fishes = pygame.sprite.Group()