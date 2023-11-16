import pygame
from parameters import *
import random
from game.fish import Fish, fishes

#funtion to draw the game background
def draw_game_background(screen):
    water = pygame.image.load("../assets/sprites/water.png")
    water.set_colorkey((0,0,0))

    #fill screen with water
    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            screen.blit(water, (x, y))

def add_fish(num_fish):
    for _ in range(num_fish):
        fishes.add(Fish(random.randint(screen_width, screen_width * 2), random.randint(0, screen_height - (tile_size * 2))))

