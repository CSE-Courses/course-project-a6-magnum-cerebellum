import pygame
import math
import music
import config
from button import Button
import game
clock = pygame.time.Clock()

def reRenderVol(volDisplay, vol, text, gameDisplay):
    volDisplay.text = text
    volDisplay.buttonText()
    gameDisplay.fill(config.black)
    volDisplay.createButton(gameDisplay)
    vol.createButton(gameDisplay)
def roundup(x):
    return int(math.ceil(x / 10.0)) * 10
def options_menu(gameDisplay):
    music_player = music.Music_Player()
    music_player.play_options()
    w, h = pygame.display.get_surface().get_size()

    gameDisplay.fill(config.black)
    #buttons = [Button("BACK", white, SPOOKY_SMALL_FONT, (0,0))]
    current_volume = music_player.get_volume()
    volumeDisplay = Button(str(roundup(math.trunc(current_volume * 100))), config.white, config.SPOOKY_SMALL_FONT, (config.display_width  /2 , config.display_height /2) ,gameDisplay)
    volume = Button("VOLUME", config.white, config.SPOOKY_SMALL_FONT, (volumeDisplay.pos[0] - 200, volumeDisplay.pos[1]) ,gameDisplay)

    buttons =[Button("BACK", config.white, pygame.font.Font("assets/fonts/CHILLER.ttf", 70), (90, 60), gameDisplay),
               Button("<", config.white, config.SPOOKY_SMALL_FONT, (config.display_width  / 2 - 80, config.display_height / 2), gameDisplay),
               Button(">", config.white, config.SPOOKY_SMALL_FONT, (config.display_width  / 2 + 80, config.display_height / 2), gameDisplay),
               Button("MUTE", config.white, config.SPOOKY_SMALL_FONT, (config.display_width  / 2, config.display_height / 2 + 100), gameDisplay),
               Button("1280 x 768", config.white, config.SPOOKY_SMALL_FONT, (config.display_width  / 2, config.display_height / 2 - 200), gameDisplay),
               Button("1400 x 900", config.white, config.SPOOKY_SMALL_FONT, (config.display_width  / 2, config.display_height / 2 - 100), gameDisplay),
               Button("Save", config.white, config.SPOOKY_SMALL_FONT, (config.display_width / 2, config.display_height / 2 + 200), gameDisplay),
               Button("Load", config.white, config.SPOOKY_SMALL_FONT,(config.display_width / 2, config.display_height / 2 + 300), gameDisplay)

              ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_p):
                    print(1111111111)
                    return
            elif (event.type == pygame.QUIT):
                pygame.quit()
                quit()

            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[0].rect.collidepoint(
                    pygame.mouse.get_pos())):
                # if(config.paused == True):
                #     print("proceeding to character selection function")
                #     character_selection(gameDisplay)
                if(config.paused == False):
                    return

            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[1].rect.collidepoint(
                    pygame.mouse.get_pos())):
                if (buttons[3].text != "UNMUTE"):
                    music_player.set_volume(current_volume - 0.10)

                # Subtracting two floats isn't exact so multiply by 100 then truncate
                if (math.trunc(current_volume * 100) > 0):
                    current_volume -= 0.10

                # Need to re-render button
                reRenderVol(volumeDisplay, volume, str(roundup(math.trunc(current_volume * 100))), gameDisplay)

            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[2].rect.collidepoint(
                    pygame.mouse.get_pos())):
                if (buttons[3].text != "UNMUTE" and current_volume <= 100):
                    music_player.set_volume(current_volume + 0.10)
                if (math.trunc(current_volume * 100) < 100):
                    current_volume += 0.10

                reRenderVol(volumeDisplay, volume, str(roundup(math.trunc(current_volume * 100))), gameDisplay)

            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[3].text == "MUTE" and buttons[
                3].rect.collidepoint(pygame.mouse.get_pos())):
                music_player.set_volume(0.0)
                buttons[3].text = "UNMUTE"
                reRenderVol(volumeDisplay, volume, str(roundup(math.trunc(current_volume * 100))), gameDisplay)

            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[3].text == "UNMUTE" and
                  buttons[3].rect.collidepoint(pygame.mouse.get_pos())):
                music_player.set_volume(current_volume)
                buttons[3].text = "MUTE"
                reRenderVol(volumeDisplay, volume, str(roundup(math.trunc(current_volume * 100))), gameDisplay)
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[4].text == "1280 x 768" and
                  buttons[4].rect.collidepoint(pygame.mouse.get_pos())):
                config.display_width = 1280
                config.display_height = 768
                pygame.display.set_mode((config.display_width, config.display_height))
                pygame.transform.scale(gameDisplay, (config.display_width, config.display_height))
                pygame.display.update()
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[5].text == "1400 x 900" and
                  buttons[5].rect.collidepoint(pygame.mouse.get_pos())):
                config.display_height = 1400
                config.display_height = 900
                pygame.display.set_mode((config.display_width, config.display_height))
                pygame.transform.scale(gameDisplay, (config.display_width, config.display_height))
                pygame.display.update()
                pygame.transform.scale(gameDisplay, (config.display_width, config.display_height))
        for button in buttons:
            Button.check_Hover(button, gameDisplay)


        pygame.display.update()
        clock.tick(15)