import pygame

class Button():
    def __init__(self, x, y):
        self.image = pygame.image.load("../assets/menu_items/buttonLong_brown.png").convert()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.pressed = False

    def draw(self, screen):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.pressed == False:
                self.pressed = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.pressed = False

        screen.blit(self.image, self.rect)


        return action