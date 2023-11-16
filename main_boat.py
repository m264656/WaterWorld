#class for the boat

import pygame
from parameters import *

class Main_Boat(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("../assets/sprites/dinghy1.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_speed = 0
        self.y_speed = 0

    def move_up(self):
        self.x_speed = PLAYER_SPEED + 1

    def move_down(self):
        self.x_speed = PLAYER_SPEED - 1

    def move_left(self):
        self.x_speed = -1 * PLAYER_SPEED

    def move_right(self):
        self.x_speed = PLAYER_SPEED

    def stop(self):
        self.x_speed = 0
        self.y_speed = 0

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        #keep on screen
        if self.x < 0:
            self.x = 0
        if self.x > screen_width - tile_size:
            self.x = screen_width - tile_size
        self.y = 20

    def draw(self, surf):
        surf.blit(self.image, self.rect)