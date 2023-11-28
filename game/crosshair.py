import pygame
from parameters import *

class Crosshair(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("../assets/sprites/crosshair.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)


    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        #keep on screen
        if self.x < 0:
            self.x = 0
        if self.x > screen_width - tile_size/3:
            self.x = screen_width - tile_size/3
        self.y = 20
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, surf):
        surf.blit(self.image, self.rect)

    def get_center(self):
        return self.x + self.width / 2, self.y + self.height / 2