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

#Main Loop
running = True
background = screen.copy()
draw_game_background(background)

#draw fish on screen
add_fish(5)

#draw player the main boat player
player = Main_Boat(screen_width/2, screen_height/2)

#set lives
lives = NUM_LIVES

while lives > 0 and running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #control our player fish with arrow keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("You pressed the key up key")
                player.increase_speed()
                fish.increase_speed()
            if event.key == pygame.K_s:
                print("You pressed the down key")
                player.decrease_speed()
                fish.decrease_speed()
            if event.key == pygame.K_a:
                print("You pressed the left key")
                player.move_left()
            if event.key == pygame.K_d:
                print("You pressed the right key")
                player.move_right()

        print(player.speed)
        if event.type == pygame.KEYUP:
            player.stop()

    #blit background
    screen.blit(background, (0, 0))

    # check if fish left the screen
    for fish in fishes:
        if fish.rect.y < -fish.rect.height:
            fishes.remove(fish)
            y = random.randint(screen_height, screen_height * 2)
            x = random.randint(0, screen_width - (tile_size * 2))
            fishes.add(Fish(x, y))

    #update the player
    player.update()
    fishes.update()

    player.draw(screen)
    fishes.draw(screen)

    #update display
    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
