import pygame
import sys
import random
import time

from game_background import draw_game_background, add_asset, increase_loop, decrease_loop, add_enemy
from parameters import *

from main_boat import Main_Boat
from main_boat2 import Main_Boat2
from main_boat3 import Main_Boat3
from enemy import Enemy, enemies

from fish import Fish, fishes
from blue_coral import Blue_Coral, blue_corals
from rock import Rock, rocks
from grassy_rock import Grassy_Rock, grassy_rocks
from orange_coral import Orange_Coral, orange_corals
from crosshair import Crosshair
from bullet import CBall, bullets
from enemy_bullet import Enemy_Ball, enemy_bullets

#initialize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((screen_width, screen_height))

#clock object and timer for game
clock = pygame.time.Clock()
clock_font = pygame.font.Font("../assets/fonts/Minangrasa.otf", 30)
counter = 60
clock_text = clock_font.render(f"{counter}", True, (50, 81, 123))

timer_event = pygame.USEREVENT +1
pygame.time.set_timer(timer_event, 1000)

#Main Loop
running = True
background = screen.copy()
draw_game_background(background)

#draw assets on screen
add_asset(5, fishes, Fish)
add_asset(3, blue_corals, Blue_Coral)
add_asset(3, rocks, Rock)
add_asset(2, grassy_rocks, Grassy_Rock)
add_asset(4, orange_corals, Orange_Coral)
add_enemy(2)

#draw player the main boat player
player = Main_Boat(screen_width/2, screen_height/2)

#draw the crosshair
aim = Crosshair(screen_width/2, screen_height/3)

#load new font to keep store
score = 0
score_font = pygame.font.Font("../assets/fonts/Minangrasa.otf", 50)

#set lives
lives = NUM_LIVES

#mouse invisible
pygame.mouse.set_visible(False)


def left_screen(objects, classification):
    for object in objects:
        if object.rect.y < -object.rect.height:
            objects.remove(object)
            y = random.randint(screen_height, screen_height * 2)
            x = random.randint(0, screen_width - (tile_size * 2))
            objects.add(classification(x, y, player.speed))

def shoot():
    bullet = CBall(player.rect.x, player.rect.y)
    print(bullet)

    bullet.velocity = (aim.rect.centerx - player.rect.centerx, aim.rect.centery - player.rect.centery)

    # length of the bullet's velocity
    magnitude = (bullet.velocity[0] ** 2 + bullet.velocity[1] ** 2) ** .5
    # limit the velocity of the bullet no matter how far the mouse is from the player
    bullet.velocity = [bullet.velocity[0] / magnitude * 2, bullet.velocity[1] / magnitude * 2]

    bullets.append(bullet)

def enemy_shoot():
    for enemy in enemies:
        enemy_bullet = Enemy_Ball(enemy.rect.x, enemy.rect.y)

        enemy_bullet.velocity =  (player.rect.centerx - enemy.rect.centerx, player.rect.centery - enemy.rect.centery)
        magnitude = (enemy_bullet.velocity[0] ** 2 + enemy_bullet.velocity[1] ** 2) ** .5
        enemy_bullet.velocity = [enemy_bullet.velocity[0] / magnitude * 5, enemy_bullet.velocity[1] / magnitude * 5]

        enemy_bullets.append(enemy_bullet)

assets = [fishes, blue_corals, rocks, grassy_rocks, orange_corals]
bullets = []
enemy_bullets = []
while lives > 0 and running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #control our player fish with arrow keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("You pressed the key up key")
                player.increase_speed()
                for asset in assets:
                    increase_loop(asset)
            if event.key == pygame.K_s:
                print("You pressed the down key")
                player.decrease_speed()
                for asset in assets:
                    decrease_loop(asset)
            if event.key == pygame.K_a:
                print("You pressed the left key")
                player.move_left()

            if event.key == pygame.K_d:
                print("You pressed the right key")
                player.move_right()

        #print(player.speed)
        if event.type == pygame.KEYUP:
            player.stop()

        #shoot with mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            shoot()
            enemy_shoot()

        #timer count down
        if event.type == timer_event:
            counter -= 1
            print(counter)
            clock_text = clock_font.render(f"{counter}", True, (50, 81, 123))
            if counter == 0:
                pygame.time.set_timer(timer_event, 0)
                running = False




    # Control crosshair with mouse
    mouse_position = pygame.mouse.get_pos()
    aim.x = mouse_position[0] - tile_size / 2
    aim.y = mouse_position[1] - tile_size / 2

    #blit background
    screen.blit(background, (0, 0))

    # update each asset
    player.update()
    fishes.update()
    blue_corals.update()
    rocks.update()
    grassy_rocks.update()
    orange_corals.update()
    aim.update()
    enemies.update()

    for bullet in bullets:
        bullet.update()
    for e in enemy_bullets:
        e.update()

    #when bullets leave screen, delete them
    for bullet in bullets:
        if bullet.x < screen_width and bullet.y < screen_height:
            continue
        else:
            bullets.remove(bullet)
        print(len(bullets))

    # check for collisions between player and fish/enemy
    result = pygame.sprite.spritecollide(player, fishes, True)
    result2 = pygame.sprite.spritecollide(player, blue_corals, True)
    result3 = pygame.sprite.spritecollide(player, rocks, True)
    result4 = pygame.sprite.spritecollide(player, grassy_rocks, True)
    result5 = pygame.sprite.spritecollide(player, orange_corals, True)

    #check for collison from enemy and bullet
    for bullet in bullets:
        attack_result = pygame.sprite.spritecollide(bullet, enemies, True)
        if attack_result:
            score += len(attack_result)
            add_enemy(len(attack_result))

    # print(result)
    if result:
        # play sounds
        #pygame.mixer.Sound.play(chomp)
        score += len(result)
        add_asset(len(result), fishes, Fish)

    if result2:
        # play sounds
        #pygame.mixer.Sound.play(hurt)
        lives -= 1
        score -= len(result2)
        add_asset(len(result2), blue_corals, Blue_Coral)
        if lives == 3:
            player = Main_Boat2(player.rect.x, player.rect.y)
        if lives == 2:
            player = Main_Boat3(player.rect.x, player.rect.y)

    if result3:
        # play sounds
        #pygame.mixer.Sound.play(hurt)
        lives -= 1
        score -= len(result3)
        add_asset(len(result3), rocks, Rock)
        if lives == 3:
            player = Main_Boat2(player.rect.x, player.rect.y)
        if lives == 2:
            player = Main_Boat3(player.rect.x, player.rect.y)

    if result4:
        # play sounds
        #pygame.mixer.Sound.play(hurt)
        lives -= 1
        score -= len(result4)
        add_asset(len(result4), grassy_rocks, Grassy_Rock)
        if lives == 3:
            player = Main_Boat2(player.rect.x, player.rect.y)
        if lives == 2:
            player = Main_Boat3(player.rect.x, player.rect.y)

    if result5:
        # play sounds
        #pygame.mixer.Sound.play(hurt)
        lives -= 1
        score -= len(result5)
        add_asset(len(result5), orange_corals, Orange_Coral)
        if lives == 3:
            player = Main_Boat2(player.rect.x, player.rect.y)
        if lives == 2:
            player = Main_Boat3(player.rect.x, player.rect.y)

    #check if objects left the screen
    left_screen(fishes, Fish)
    left_screen(blue_corals, Blue_Coral)
    left_screen(rocks, Rock)
    left_screen(grassy_rocks, Grassy_Rock)
    left_screen(orange_corals, Orange_Coral)
    left_screen(enemies, Enemy)

    for bullet in bullets:
        bullet.draw(screen)
    for e in enemy_bullets:
        e.draw(screen)
    enemies.draw(screen)
    player.draw(screen)
    aim.draw(screen)
    fishes.draw(screen)
    blue_corals.draw(screen)
    rocks.draw(screen)
    grassy_rocks.draw(screen)
    orange_corals.draw(screen)

    # update score on screen
    text = score_font.render(f"{score}", True, (50, 81, 123))
    screen.blit(text, (screen_width - text.get_width() / 2 - 40, screen_height / 10 - text.get_height() / 2))

    #update timer on screen
    clock_text = clock_font.render(f"Time Remaining: {counter}", True, (50,81,123))
    screen.blit(clock_text, (clock_text.get_width()/10, screen_height - 2 * text.get_height()))

    pygame.display.flip()

    #clock time limit for game
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
