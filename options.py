import pygame
import music
# from davis import gameDisplay, roundup
from important_funcs import funcs, gameDisplay
import config
from button import Button
import math
from important_funcs import funcs
import mainmenu


class option:

    def options_menu(self):

        music_player = music.Music_Player()
        music_player.play_normal()
        w, h = pygame.display.get_surface().get_size()

        gameDisplay.fill(config.black)
        # buttons = [Button("BACK", white, SPOOKY_SMALL_FONT, (0,0))]
        current_volume = music_player.get_volume()
        volumeDisplay = Button(str(funcs.roundup(math.trunc(current_volume * 100))), config.white, config.SPOOKY_SMALL_FONT,
                               (w / 2, h / 2), gameDisplay)
        volume = Button("VOLUME", config.white, config.SPOOKY_SMALL_FONT,
                        (volumeDisplay.pos[0] - 200, volumeDisplay.pos[1]), gameDisplay)

        buttons = [Button("BACK", config.white, pygame.font.Font("assets/fonts/CHILLER.ttf", 70), (90, 60), gameDisplay),
                   Button("<", config.white, config.SPOOKY_SMALL_FONT, (w / 2 - 80, h / 2), gameDisplay),
                   Button(">", config.white, config.SPOOKY_SMALL_FONT, (w / 2 + 80, h / 2), gameDisplay),
                   Button("MUTE", config.white, config.SPOOKY_SMALL_FONT, (w / 2, h / 2 + 100), gameDisplay),
                   Button("1280 x 768", config.white, config.SPOOKY_SMALL_FONT, (w / 2, h / 2 - 200), gameDisplay),
                   Button("1400 x 1050", config.white, config.SPOOKY_SMALL_FONT, (w / 2, h / 2 - 100), gameDisplay)]
        while True:

            for event in pygame.event.get():
                print(event)
                if (event.type == pygame.QUIT):
                    pygame.quit()
                    quit()

                elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[0].rect.collidepoint(
                        pygame.mouse.get_pos())):
                    main_menu()

                elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[1].rect.collidepoint(
                        pygame.mouse.get_pos())):
                    if (buttons[3].text != "UNMUTE"):
                        music_player.set_volume(current_volume - 0.10)

                    # Subtracting two floats isn't exact so multiply by 100 then truncate
                    if (math.trunc(current_volume * 100) > 0):
                        current_volume -= 0.10

                    # Need to re-render button
                    funcs.reRenderVol(volumeDisplay, volume, str(funcs.roundup(math.trunc(current_volume * 100))))

                elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[2].rect.collidepoint(
                        pygame.mouse.get_pos())):
                    if (buttons[3].text != "UNMUTE" and current_volume <= 100):
                        music_player.set_volume(current_volume + 0.10)
                    if (math.trunc(current_volume * 100) < 100):
                        current_volume += 0.10

                    funcs.reRenderVol(volumeDisplay, volume, str(funcs.roundup(math.trunc(current_volume * 100))))

                elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[3].text == "MUTE" and buttons[
                    3].rect.collidepoint(pygame.mouse.get_pos())):
                    music_player.set_volume(0.0)
                    buttons[3].text = "UNMUTE"
                    funcs.reRenderVol(volumeDisplay, volume, str(funcs.roundup(math.trunc(current_volume * 100))))

                elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[3].text == "UNMUTE" and
                      buttons[3].rect.collidepoint(pygame.mouse.get_pos())):
                    music_player.set_volume(current_volume)
                    buttons[3].text = "MUTE"
                    funcs.reRenderVol(volumeDisplay, volume, str(funcs.roundup(math.trunc(current_volume * 100))))
                elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[4].text == "1280 x 768" and
                      buttons[4].rect.collidepoint(pygame.mouse.get_pos())):
                    pygame.display.set_mode((1280, 768))
                    pygame.transform.scale(gameDisplay, (1280, 768))
                    pygame.display.update()


                    mainmenu.main_menu()
                elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[5].text == "1400 x 1050" and
                      buttons[5].rect.collidepoint(pygame.mouse.get_pos())):
                    pygame.display.set_mode((1400, 1050))
                    pygame.transform.scale(gameDisplay, (1400, 1050))
                    pygame.display.update()


                    mainmenu.main_menu()
                    pygame.transform.scale(gameDisplay, (1400, 1050))
