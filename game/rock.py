import pygame
from parameters import *

class Rock(pygame.sprite.Sprite):
    def __init__(self, x, y, speed=player_speed):
        super().__init__()
        self.image = pygame.image.load("../assets/sprites/rock1.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = speed
        self.rect.center = (x,y)

    def increase_speed(self):
        if self.speed < MAX_SPEED:
            self.speed += 1

    def decrease_speed(self):
        if self.speed > MIN_SPEED:
            self.speed -= 1
        else:
            self.speed = MIN_SPEED

    def update(self):
        #update y position of coral
        self.y -= self.speed
        self.rect.y = self.y

    def draw(self, surf):
        surf.blit(self.image, self.rect)

rocks = pygame.sprite.Group()