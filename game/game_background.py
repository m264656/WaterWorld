import pygame
from parameters import *
import random
from fish import Fish, fishes
from blue_coral import Blue_Coral, blue_corals

#funtion to draw the game background
def draw_game_background(screen):
    water = pygame.image.load("../assets/sprites/water.png").convert()

    #fill screen with water
    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            screen.blit(water, (x, y))

def add_fish(num_fish):
    for _ in range(num_fish):
        fishes.add(Fish(random.randint(screen_width, screen_width * 2), random.randint(0, screen_height - (tile_size * 2))))

def add_blue_corals(num_bcorals):
    for _ in range(num_bcorals):
        blue_corals.add(Blue_Coral(random.randint(screen_width, screen_width * 2), random.randint(0, screen_height - (tile_size * 2))))
