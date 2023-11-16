import pygame
import sys
import random

from fish import Fish, fishes
from game_background import draw_game_background, add_fish
from parameters import *
from main_boat import Main_Boat

#initialize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((screen_width, screen_height))

#clock object
clock = pygame.time.Clock()

#draw fish on screen
add_fish(5)

#draw player the main boat player
player = Main_Boat(screen_width/2, screen_height/2)
