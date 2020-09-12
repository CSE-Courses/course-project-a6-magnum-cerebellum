import time
import random
import pygame

pygame.init()
 
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
SPOOKY_BIG_FONT = pygame.font.Font("assets/fonts/CHILLER.ttf", 115)
SPOOKY_SMALL_FONT = pygame.font.Font("assets/fonts/CHILLER.ttf", 40)

display_width = 1024
display_height = 768
 
gameDisplay = pygame.display.set_mode((display_width,display_height))
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
 
def main_menu():

    intro = True

    buttons = [Button("START", white, SPOOKY_SMALL_FONT, ((display_width/2),(display_height/2))),
    Button("OPTIONS", white, SPOOKY_SMALL_FONT, ((display_width/2),(display_height/1.5))),
    Button("QUIT", white, SPOOKY_SMALL_FONT, ((display_width/2),(display_height/1.25)))]

    while intro:
        gameDisplay.fill(black)
        TextSurf, TextRect = render_text("Davis Hall", SPOOKY_BIG_FONT, red)
        TextRect.center = ((display_width/2),(display_height/6))
        gameDisplay.blit(TextSurf, TextRect)
        
        for event in pygame.event.get():
            print(event)
            if (event.type == pygame.QUIT or 
            (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[2].rect.collidepoint(pygame.mouse.get_pos()))):
                pygame.quit()
                quit()
                
        for button in buttons:
            if button.rect.collidepoint(pygame.mouse.get_pos()):
                button.color = red
            else:
                button.color = white
            button.createButton()

        pygame.display.update()
        clock.tick(15)
        
main_menu()


quit()