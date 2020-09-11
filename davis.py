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
  
 
def render_text(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()
 
def main_menu():

    intro = True

    START_BUTTON, START_BUTTON_RECT = render_text("START", SPOOKY_SMALL_FONT, white)
    OPTIONS_BUTTON, OPTIONS_BUTTON_RECT = render_text("OPTIONS",SPOOKY_SMALL_FONT, white)
    QUIT_BUTTON, QUIT_BUTTON_RECT = render_text("EXIT", SPOOKY_SMALL_FONT, white)

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(black)
        TextSurf, TextRect = render_text("Davis Hall", SPOOKY_BIG_FONT, red)
        START_BUTTON_RECT.center = ((display_width/2),(display_height/2))
        OPTIONS_BUTTON_RECT.center = ((display_width/2),(display_height/1.5))
        QUIT_BUTTON_RECT.center = ((display_width/2),(display_height/1.25))
        TextRect.center = ((display_width/2),(display_height/6))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(START_BUTTON, START_BUTTON_RECT)
        gameDisplay.blit(OPTIONS_BUTTON, OPTIONS_BUTTON_RECT)
        gameDisplay.blit(QUIT_BUTTON, QUIT_BUTTON_RECT)

        pygame.display.update()
        clock.tick(15)
        
        
    
    
main_menu()


quit()