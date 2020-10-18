import time
import random
import pygame
import math
import music
import config
from health import Bar
from button import Button
from player import Player
from character import Character
from character_UI import char_ui
import inventory
from inventory import inventoryMain
import game

pygame.init()


music_player = music.Music_Player()
music_player.set_volume(1.0)

gameDisplay = pygame.display.set_mode((config.display_width, config.display_height))
pygame.display.set_caption('Davis Hall Escape Simulator 2020')
clock = pygame.time.Clock()

def roundup(x):
    return int(math.ceil(x / 10.0)) * 10

def render_text(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

class Checkbox:
    def __init__(self):
        self.draw()

    def draw(self):
        pygame.draw.circle(gameDisplay, config.white, (150,150), 75)

def reRenderVol(volDisplay, vol, text):
    volDisplay.text = text
    volDisplay.buttonText()
    gameDisplay.fill(config.black)
    volDisplay.createButton(gameDisplay)
    vol.createButton(gameDisplay)

def destroy(self, name_of_class):
    name_of_class.List.remove(self)
    del self

def main_menu():

    intro = True
    buttons = [Button("START", config.white, config.SPOOKY_SMALL_FONT, ((config.display_width/2),(config.display_height/2)), gameDisplay),
    Button("OPTIONS", config.white, config.SPOOKY_SMALL_FONT, ((config.display_width/2),(config.display_height/1.5)), gameDisplay),
    Button("QUIT", config.white, config.SPOOKY_SMALL_FONT, ((config.display_width/2),(config.display_height/1.20)), gameDisplay),
    Button("inventoryPreview", config.white, config.SPOOKY_SMALL_FONT, ((config.display_width/2),(config.display_height/1.1)), gameDisplay),
    Button("Rendering Demo", config.white, config.SPOOKY_SMALL_FONT, ((config.display_width/2),(config.display_height-500)), gameDisplay)]
    gameDisplay.fill(config.black)
    
    TextSurf, TextRect = render_text("Davis Hall", config.SPOOKY_BIG_FONT, config.red)
    TextRect.center = ((round(config.display_width/2)),(round(config.display_height/5)))
    set_image("assets/images/very_scary_davis.jpg", gameDisplay)
    gameDisplay.blit(TextSurf, TextRect)
    music_player.play_main()

    while intro:
        for event in pygame.event.get():
           
            if (event.type == pygame.QUIT or 
            (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[2].rect.collidepoint(pygame.mouse.get_pos()))):
                pygame.quit()
                quit()

            # When START button is selected, begin a new game.
            # For now, this will load into the mockup image, then we'll place things accordingly.
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[0].rect.collidepoint(pygame.mouse.get_pos())):
                music_player.stop()
                game_start()

            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[1].rect.collidepoint(pygame.mouse.get_pos())):
                music_player.stop()
                options_menu()
            #Temporary inventory preview button 
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[3].rect.collidepoint(pygame.mouse.get_pos())):
                inventoryMain()
            #Temporary game rendering prototype Button
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[4].rect.collidepoint(pygame.mouse.get_pos())):
                game.GameMain(gameDisplay)

        for button in buttons:
            Button.check_Hover(button, gameDisplay)

        pygame.display.update()
        clock.tick(15)

# This function will effectively kick off gameplay - should load into character selection screen first.
# For now the mockup will serve as a visual placeholder.
def game_start():
    music_player = music.Music_Player()
    music_player.play_ambtrack1()

    gameDisplay.fill(config.black)
    buttons = [Button("BACK", config.blue, pygame.font.Font("assets/fonts/CHILLER.ttf", 70), (90, 60), gameDisplay)]
    set_image("assets/images/Menu_Mockup_1.1.jpg", gameDisplay)
    Bar(config.black, config.SPOOKY_SMALLER_FONT, (830, 150), gameDisplay)  # pos (800, 290) is close for non demo

    #Instantiating a demo character here since selection screen is not implemented yet
    demoChar = Character("student")
    char_ui(config.SPOOKY_SMALLER_FONT, (900, 50), "Joe Gamer", demoChar, gameDisplay)

    # I imagine we will move this into a larger, separate file for actual gameplay

    # button events
    while True:

        for event in pygame.event.get():
            print(event)
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[0].rect.collidepoint(pygame.mouse.get_pos())):
                main_menu()

        for button in buttons:
            Button.check_Hover(button, gameDisplay)

        pygame.display.update()
        clock.tick(15)

def options_menu():
    music_player = music.Music_Player()
    music_player.play_options()
    w, h = pygame.display.get_surface().get_size()

    gameDisplay.fill(config.black)
    #buttons = [Button("BACK", white, SPOOKY_SMALL_FONT, (0,0))]
    current_volume = music_player.get_volume()
    volumeDisplay = Button(str(roundup(math.trunc(current_volume * 100))), config.white, config.SPOOKY_SMALL_FONT, (w/2,h/2),gameDisplay)
    volume = Button("VOLUME", config.white, config.SPOOKY_SMALL_FONT, (volumeDisplay.pos[0] - 200, volumeDisplay.pos[1]),gameDisplay)

    buttons =[Button("BACK", config.white, pygame.font.Font("assets/fonts/CHILLER.ttf", 70), (90, 60), gameDisplay),
    Button("<", config.white, config.SPOOKY_SMALL_FONT, (w/2-80,h/2), gameDisplay),
    Button(">", config.white, config.SPOOKY_SMALL_FONT, (w/2+80,h/2), gameDisplay),
    Button("MUTE", config.white, config.SPOOKY_SMALL_FONT, (w/2,h/2+100), gameDisplay),
    Button("1280 x 768", config.white, config.SPOOKY_SMALL_FONT, (w / 2, h / 2 - 200), gameDisplay),
    Button("1400 x 1050", config.white, config.SPOOKY_SMALL_FONT, (w / 2, h / 2 - 100), gameDisplay)]


    backButton = Button("BACK", config.white, pygame.font.Font("assets/fonts/CHILLER.ttf", 70), (90, 60), gameDisplay)
    
    while True :
        
        for event in pygame.event.get():
            print(event)
            if (event.type == pygame.QUIT) :
                pygame.quit()
                quit()

            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[0].rect.collidepoint(pygame.mouse.get_pos())):
                main_menu()

            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[1].rect.collidepoint(pygame.mouse.get_pos())):
                if (buttons[3].text != "UNMUTE"):
                    music_player.set_volume(current_volume - 0.10)
                
                # Subtracting two floats isn't exact so multiply by 100 then truncate
                if (math.trunc(current_volume*100) > 0):
                    current_volume -= 0.10

                #Need to re-render button
                reRenderVol(volumeDisplay, volume, str(roundup(math.trunc(current_volume*100))))

            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[2].rect.collidepoint(pygame.mouse.get_pos())):
                if (buttons[3].text != "UNMUTE" and current_volume <= 100):
                    music_player.set_volume(current_volume + 0.10)
                if (math.trunc(current_volume*100) < 100):
                    current_volume += 0.10

                reRenderVol(volumeDisplay, volume, str(roundup(math.trunc(current_volume*100))))

            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[3].text == "MUTE" and buttons[3].rect.collidepoint(pygame.mouse.get_pos())):
                music_player.set_volume(0.0)
                buttons[3].text = "UNMUTE"
                reRenderVol(volumeDisplay, volume, str(roundup(math.trunc(current_volume*100))))

            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[3].text == "UNMUTE" and buttons[3].rect.collidepoint(pygame.mouse.get_pos())):
                music_player.set_volume(current_volume)
                buttons[3].text = "MUTE"
                reRenderVol(volumeDisplay, volume, str(roundup(math.trunc(current_volume*100))))
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[4].text == "1280 x 768" and
                  buttons[4].rect.collidepoint(pygame.mouse.get_pos())):
                pygame.display.set_mode((1280, 768))
                pygame.transform.scale(gameDisplay, (1280, 768))
                pygame.display.update()
                main_menu()
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[5].text == "1400 x 1050" and
                  buttons[5].rect.collidepoint(pygame.mouse.get_pos())):
                pygame.display.set_mode ((1400, 1050))
                pygame.transform.scale(gameDisplay, (1400, 1050))
                pygame.display.update()
                main_menu()
                pygame.transform.scale(gameDisplay,(1400,1050))

        for button in buttons:
            Button.check_Hover(button, gameDisplay)

        pygame.display.update()
        clock.tick(15)

    # This will load an image and then set it to the passed display.
def set_image(image, display):
    image_surface = pygame.image.load(image)
    display.blit(image_surface, (0, 0))

main_menu()


quit()
