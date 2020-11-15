import pygame
import math
import music
import pickle
import config
from health import Bar
from button import Button
import utilities
import game
from character import Character, create_all_characters, random_character
from enemies import Enemy, random_enemy
from player import Player
from character_selection import character_selection
import intro_screen
from options_menu import options_menu
import battle_blit
clock = pygame.time.Clock()

def main_menu(gameDisplay, music_player):
    intro = True
    # gameDisplay.fill(config.black)
    # TextSurf, TextRect = utilities.render_text("Davis Hall", config.SPOOKY_BIG_FONT, config.red)
    # TextRect.center = ((round(config.display_width/2)),(round(config.display_height/5)))
    # utilities.set_image("assets/images/very_scary_davis.jpg", gameDisplay)
    # gameDisplay.blit(TextSurf, TextRect)
    music_player.play_main()
    buttons = [
        Button("START", config.white, config.SPOOKY_SMALL_FONT,
               ((config.display_width / 2), (config.display_height / 2)),
               gameDisplay),
        Button("OPTIONS", config.white, config.SPOOKY_SMALL_FONT,
               ((config.display_width / 2), (config.display_height / 1.5)), gameDisplay),
        Button("QUIT", config.white, config.SPOOKY_SMALL_FONT,
               ((config.display_width / 2), (config.display_height / 1.20)),
               gameDisplay),
        Button("Rendering Demo", config.white, config.SPOOKY_SMALL_FONT,
               ((config.display_width/2),(config.display_height-500)), gameDisplay),
        Button("Battle Demo", config.white, config.SPOOKY_SMALL_FONT, 
                ((config.display_width/2),(config.display_height/1.3)), gameDisplay),]

    while intro:
        gameDisplay.fill(config.black)
        TextSurf, TextRect = utilities.render_text("Davis Hall", config.SPOOKY_BIG_FONT, config.red)
        TextRect.center = ((round(config.display_width/2)),(round(config.display_height/5)))
        utilities.set_image("assets/images/very_scary_davis.jpg", gameDisplay)
        gameDisplay.blit(TextSurf, TextRect)
        

        for event in pygame.event.get():
            if (event.type == pygame.QUIT or
                    (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[2].text == "QUIT" and buttons[2].rect.collidepoint
                        (pygame.mouse.get_pos()))):
                pygame.quit()
                quit()

            # When START button is selected, begin a new game.
            # For now, this will load into the mockup image, then we'll place things accordingly.
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[0].rect.collidepoint(pygame.mouse.get_pos())):
                music_player.stop()
                intro_screen.main()
                character_selection(gameDisplay)
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[1].rect.collidepoint(pygame.mouse.get_pos())):
                music_player.stop()
                options_menu(gameDisplay)
            #Temporary game rendering prototype Button
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[3].rect.collidepoint(pygame.mouse.get_pos())):
                game.GameMain(gameDisplay, "Techie")

            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[4].rect.collidepoint(pygame.mouse.get_pos())):
                music_player.stop() 
                dummy_player = Player(random_character())
                dummy_enemy = Enemy(random_enemy())
                
                battle_blit.battleMain(dummy_player, dummy_enemy, gameDisplay)



        for button in buttons:
            Button.check_Hover(button, gameDisplay)

        pygame.display.update()
        clock.tick(15)

# This function will effectively kick off gameplay - should load into character selection screen first.
# For now the mockup will serve as a visual placeholder.

