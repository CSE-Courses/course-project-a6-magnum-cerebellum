import music
import pygame
from button import Button
import config
import important_funcs
from important_funcs import funcs
from inventory import inventoryMain
import options

clock = pygame.time.Clock()
music_player = music.Music_Player()
music_player.set_volume(1.0)

def main_menu():
    w, h = pygame.display.get_surface().get_size()

    intro = True
    buttons = [Button("START", config.white, config.SPOOKY_SMALL_FONT,
                      ((w / 2), (h / 2)), important_funcs.gameDisplay),
               Button("OPTIONS", config.white, config.SPOOKY_SMALL_FONT,
                      ((w / 2), (h / 1.5)), important_funcs.gameDisplay),
               Button("QUIT", config.white, config.SPOOKY_SMALL_FONT,
                      ((w / 2), (h / 1.20)), important_funcs.gameDisplay),
               Button("inventoryPreview", config.white, config.SPOOKY_SMALL_FONT,
                      ((w / 2), (h / 1.1)), important_funcs.gameDisplay)]

    important_funcs.gameDisplay.fill(config.black)

    TextSurf, TextRect = funcs.render_text("Davis Hall", config.SPOOKY_BIG_FONT, config.red)

    TextRect.center = ((round(w / 2)), (round(h / 5)))
    important_funcs.gameDisplay.blit(TextSurf, TextRect)
    music_player.play_intro()

    while intro:
        for event in pygame.event.get():

            if (event.type == pygame.QUIT or
                    (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[2].rect.collidepoint(
                        pygame.mouse.get_pos()))):
                pygame.quit()
                quit()

            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[1].rect.collidepoint(
                    pygame.mouse.get_pos())):

                a = options.options_menu()
                pygame.display.update()

            # Temporary inventory preview button
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[3].rect.collidepoint(
                    pygame.mouse.get_pos())):
                inventoryMain()
            # Temporary inventory preview button

        for button in buttons:
            Button.check_Hover(button, important_funcs.gameDisplay)

        pygame.display.update()
        clock.tick(15)
