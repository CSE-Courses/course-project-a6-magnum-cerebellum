import time
import random
import pygame
import math

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
SPOOKY_BIG_FONT = pygame.font.Font("assets/fonts/CHILLER.ttf", 120)
SPOOKY_SMALL_FONT = pygame.font.Font("assets/fonts/CHILLER.ttf", 60)

display_width = 1024
display_height = 768
resolution = pygame.display.Info()
width = resolution.current_w
height = resolution.current_h

gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.RESIZABLE)
pygame.display.set_caption('Davis Hall Escape Simulator 2020')
clock = pygame.time.Clock()


class Button:

    def __init__(self, text, color, font, pos):
        self.text = text
        self.color = color
        self.font = font
        self.pos = pos

        self.set_rect()
        self.createButton()

    def buttonText(self):
        self.rend = self.font.render(self.text, True, self.color)

    def set_rect(self):
        self.buttonText()
        self.rect = self.rend.get_rect()
        self.rect.center = self.pos

    def createButton(self):
        self.buttonText()
        gameDisplay.blit(self.rend, self.rect)


def render_text(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def check_Hover(button):
    if button.rect.collidepoint(pygame.mouse.get_pos()):
        button.color = red
    else:
        button.color = white
    button.createButton()


def main_menu():
    intro = True

    buttons = [Button("START", white, SPOOKY_SMALL_FONT, ((display_width / 2), (display_height / 2))),
               Button("OPTIONS", white, SPOOKY_SMALL_FONT, ((display_width / 2), (display_height / 1.5))),
               Button("QUIT", white, SPOOKY_SMALL_FONT, ((display_width / 2), (display_height / 1.20)))]
    gameDisplay.fill(black)

    TextSurf, TextRect = render_text("Davis Hall", SPOOKY_BIG_FONT, red)
    TextRect.center = ((display_width / 2), (display_height / 5))
    set_image("assets/images/very_scary_davis.jpg", gameDisplay)
    gameDisplay.blit(TextSurf, TextRect)


    while intro:

        for event in pygame.event.get():
            print(event)
            if (event.type == pygame.QUIT or
                    (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[2].rect.collidepoint(
                        pygame.mouse.get_pos()))):
                pygame.quit()
                quit()

            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[1].rect.collidepoint(
                    pygame.mouse.get_pos())):
                gameDisplay.fill(black)
                options_menu()

        for button in buttons:
            check_Hover(button)

        pygame.display.update()
        clock.tick(15)


def options_menu():
    # buttons = [Button("BACK", white, SPOOKY_SMALL_FONT, (0,0))]

    backButton = Button("BACK", white, pygame.font.Font("assets/fonts/CHILLER.ttf", 70), (90, 60))

    videoButton = Button("Video", white, pygame.font.Font("assets/fonts/CHILLER.ttf", 70), (190, 200))

    fullscreenButton = Button("FullScreen", white, pygame.font.Font("assets/fonts/CHILLER.ttf", 70), (190, 300))

    while True:
        for event in pygame.event.get():
            print(event)
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()

            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and backButton.rect.collidepoint(
                    pygame.mouse.get_pos())):
                main_menu()
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and videoButton.rect.collidepoint(
                    pygame.mouse.get_pos())):
                main_menu()
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and fullscreenButton.rect.collidepoint(
                    pygame.mouse.get_pos())):
                gameDisplay = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

        check_Hover(backButton)
        check_Hover(videoButton)  #
        check_Hover(fullscreenButton)  #

        pygame.display.update()
        clock.tick(15)

# This will load an image and then set it to the passed display.
def set_image(image, display):
    image_surface = pygame.image.load(image)
    display.blit(image_surface, (0, 0))


main_menu()

quit()