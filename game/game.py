import pygame
import sys
import random

from fish import Fish, fishes
from game_background import draw_game_background, add_fish, add_blue_corals
from parameters import *
from main_boat import Main_Boat
from blue_coral import Blue_Coral, blue_corals

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
add_blue_corals(5)

#draw player the main boat player
player = Main_Boat(screen_width/2, screen_height/2)

#load new font to keep store
score = 0
score_font = pygame.font.Font("../assets/fonts/Minangrasa.otf", 50)

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
                #blue_coral.increase_speed()
            if event.key == pygame.K_s:
                print("You pressed the down key")
                player.decrease_speed()
                fish.decrease_speed()
                #Blue_Coral.decrease_speed()
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

    # update the player
    player.update()
    fishes.update()
    blue_corals.update()

    # check for collisions between player and fish/enemy
    result = pygame.sprite.spritecollide(player, fishes, True)
    result2 = pygame.sprite.spritecollide(player, blue_corals, True)

    # print(result)
    if result:
        # play sounds
        #pygame.mixer.Sound.play(chomp)
        score += len(result)
        add_fish(len(result))

    if result2:
        # play sounds
        #pygame.mixer.Sound.play(hurt)
        lives -= len(result2)
        score -= len(result2)
        add_blue_corals(len(result2))

    # check if fish left the screen
    for fish in fishes:
        if fish.rect.y < -fish.rect.height:
            fishes.remove(fish)
            y = random.randint(screen_height, screen_height * 2)
            x = random.randint(0, screen_width - (tile_size * 2))
            fishes.add(Fish(x, y, player.speed))

    #check if blue corals left the screen
    for b_coral in blue_corals:
        if b_coral.rect.y < -b_coral.rect.height:
            blue_corals.remove(b_coral)
            y = random.randint(screen_height, screen_height * 2)
            x = random.randint(0, screen_width - (tile_size * 2))
            blue_corals.add(Blue_Coral(x, y, player.speed))

    player.draw(screen)
    fishes.draw(screen)
    blue_corals.draw(screen)

    # update score on screen
    text = score_font.render(f"{score}", True, (50, 81, 123))
    screen.blit(text, (screen_width - text.get_width() / 2 - 40, screen_height / 10 - text.get_height() / 2))

    pygame.display.flip()

    clock.tick(60)

# create new background when game over
screen.blit(background, (0, 0))

# show game over message
message = score_font.render("GAME OVER", True, (0, 0, 0))
screen.blit(message, (screen_width / 2 - message.get_width() / 2, screen_height / 2))

# show final score
score_text = score_font.render(f"Score: {score}", True, (0, 0, 0))
screen.blit(score_text,(screen_width / 2 - score_text.get_width() / 2, screen_height / 2 + score_text.get_height()))

# update display
pygame.display.flip()

#update display
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
