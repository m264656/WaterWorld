import pygame
from parameters import *

class Enemy_Ball(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("../assets/sprites/cannonBall.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.velocity = [0,0]


    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, surf):
        surf.blit(self.image, self.rect)

enemy_bullets = pygame.sprite.Group()

# enemy_bullets.add(Enemy_Ball(a....))