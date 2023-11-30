import pygame
from parameters import *
import random

from enemy import Enemy, enemies

#funtion to draw the game background
def draw_game_background(screen):
    water = pygame.image.load("../assets/sprites/water.png").convert()

    #fill screen with water
    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            screen.blit(water, (x, y))

def increase_loop(category):
    for object in category:
        object.increase_speed()

def decrease_loop(category):
    for object in category:
        object.decrease_speed()

def add_asset(num, asset, method):
    random.seed = random.randint(0, 1000)
    print(random.seed)
    for _ in range(num):
        asset.add(method(random.randint(0, screen_width + tile_size), random.randint(screen_height, screen_height + 100)))

def add_enemy(num):
    random.seed = random.randint(0, 1000)
    print(random.seed)
    for _ in range(num):
        enemies.add(Enemy(random.randint(0, screen_width + tile_size), random.randint(screen_height, screen_height + 60)))
