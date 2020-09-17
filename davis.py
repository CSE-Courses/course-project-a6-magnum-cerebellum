import time
import random
import pygame
import math

pygame.init()
 
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
SPOOKY_BIG_FONT = pygame.font.Font("assets/fonts/CHILLER.ttf", 120)
SPOOKY_SMALL_FONT = pygame.font.Font("assets/fonts/CHILLER.ttf", 60)

display_width = 1024
display_height = 768
pygame.mixer.music.set_volume(1)
 
gameDisplay = pygame.display.set_mode((display_width, display_height))
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
    pygame.mixer.init()
    pygame.mixer.music.load("assets/sound/sandstorm.mp3")
    pygame.mixer.music.play()
    buttons = [Button("START", white, SPOOKY_SMALL_FONT, ((display_width/2),(display_height/2))),
    Button("OPTIONS", white, SPOOKY_SMALL_FONT, ((display_width/2),(display_height/1.5))),
    Button("QUIT", white, SPOOKY_SMALL_FONT, ((display_width/2),(display_height/1.20)))]
    gameDisplay.fill(black)
    
    TextSurf, TextRect = render_text("Davis Hall", SPOOKY_BIG_FONT, red)
    TextRect.center = ((display_width/2),(display_height/5))
    gameDisplay.blit(TextSurf, TextRect)

    while intro:
        
        for event in pygame.event.get():
            print(event)
            if (event.type == pygame.QUIT or 
            (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[2].rect.collidepoint(pygame.mouse.get_pos()))):
                pygame.quit()
                quit()
            
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[1].rect.collidepoint(pygame.mouse.get_pos())):
                options_menu()
                
                
        for button in buttons:
            check_Hover(button)

        pygame.display.update()
        clock.tick(15)

def options_menu():
    gameDisplay.fill(black)
    #buttons = [Button("BACK", white, SPOOKY_SMALL_FONT, (0,0))]
    current_volume = pygame.mixer.music.get_volume()
    volumeDisplay = Button(str(current_volume), white, SPOOKY_SMALL_FONT, (display_width/2,display_height/2))
    buttons =[Button("BACK", white, pygame.font.Font("assets/fonts/CHILLER.ttf", 70), (90, 60)),
    Button("<", white, SPOOKY_SMALL_FONT, (display_width/2-150,display_height/2)),
    Button(">", white, SPOOKY_SMALL_FONT, (display_width/2+150,display_height/2)),
    Button("MUTE", white, SPOOKY_SMALL_FONT, (display_width/2,display_height/2+100))]


    while True :
        
        for event in pygame.event.get():
            print(event)
            if (event.type == pygame.QUIT) :
                pygame.quit()
                quit()

            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[0].rect.collidepoint(pygame.mouse.get_pos())):
                main_menu()
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[1].rect.collidepoint(pygame.mouse.get_pos())):
                pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()-0.1)
                volumeDisplay.text = str(pygame.mixer.music.get_volume())
                volumeDisplay.buttonText()
               # volumeDisplay.createButton()
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[2].rect.collidepoint(pygame.mouse.get_pos())):
                pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()+0.1)
                volumeDisplay.text = str(pygame.mixer.music.get_volume())
                volumeDisplay.buttonText()
               # volumeDisplay.createButton()
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[3].text == "MUTE" and buttons[3].rect.collidepoint(pygame.mouse.get_pos())):
                pygame.mixer.music.set_volume(0)
                volumeDisplay.text = str(pygame.mixer.music.get_volume())
                buttons[3].text = "UNMUTE"
                buttons[3].buttonText()
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[3].text == "UNMUTE" and buttons[3].rect.collidepoint(pygame.mouse.get_pos())):
                pygame.mixer.music.set_volume(current_volume)
                volumeDisplay.text = str(current_volume)
                buttons[3].text = "MUTE"
                buttons[3].buttonText()

        for button in buttons:
            check_Hover(button)

        pygame.display.update()
        clock.tick(15)

main_menu()


quit()