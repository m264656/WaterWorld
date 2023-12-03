import pygame
from parameters import *
import random

from enemy import Enemy, enemies

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

def add_asset(num, group, class_name):
    for _ in range(num):
        group.add(class_name(random.randint(0, screen_width + tile_size), random.randint(screen_height, screen_height + 500)))

def add_enemy(num):
    for _ in range(num):
        enemies.add(Enemy(random.randint(0, screen_width + tile_size), random.randint(screen_height, screen_height + 500)))
