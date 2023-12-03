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
        self.speed = player_speed
        self.x_speed = 0
        self.y_speed = 0
        self.score = 0

    def increase_speed(self):
        if self.speed < MAX_SPEED:
            self.speed += 1

    def decrease_speed(self):
        if self.speed > MIN_SPEED:
            self.speed -= 1
        else:
            self.speed = MIN_SPEED

    def move_left(self):
        self.x_speed = -self.speed

    def move_right(self):
        self.x_speed = self.speed

    def stop(self):
        self.x_speed = 0
        self.y_speed = 0

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

        # TODO: accept bullets sprite group into this method
        # Collsioncheck --> spritecollideany(self, bullets)
        # if spritecollideany(self, bullets): then add to score

        # if self.check_collision(assets):
        #     self.image = pygame.image.load("../assets/sprites/dinghy2.png").convert()
        #     # TODO: iterate through damaged images
        #
        # if self.check_collision(bullets):
        #     self.score += 1

    def draw(self, surf):
        surf.blit(self.image, self.rect)


