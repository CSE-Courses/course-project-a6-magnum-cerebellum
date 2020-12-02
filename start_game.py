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
import game
from character import Character, create_all_characters, random_character
from enemies import Enemy, random_enemy
from player import Player

#from assets import character_images
from os import listdir
from os.path import isfile, join
import map_blit
import transitions

from assets import character_images
import utilities
# from os import listdirtes
# from os.path import isfile, join

clock = pygame.time.Clock()
paused = False


def game_start(player, gameDisplay):
    music_player = music.Music_Player()
    music_player.play_ambtrack1()
    w, h = pygame.display.get_surface().get_size()
    gameDisplay = transitions.transistion_character_selection_gameplay(pygame.display.get_surface(), player)
    gameDisplay.fill(config.black)
    buttons = [Button("BACK", config.blue, pygame.font.Font("assets/fonts/CHILLER.ttf", 70), (90, 60), gameDisplay),]
    utilities.set_image("assets/images/Menu_Mockup_1.1.jpg", gameDisplay)
    map = map_blit.Map("View Map", (700,0))
    map.blit(gameDisplay)

    while True:

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[0].rect.collidepoint(
                    pygame.mouse.get_pos())):
                main_menu()
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and map.rect.collidepoint(
                    pygame.mouse.get_pos())):
                map.enter(gameDisplay)

        for button in buttons:
            Button.check_Hover(button, gameDisplay)
        map.check_hover()
        pygame.display.update()
        clock.tick(15)
#unused
def start_game_play(player, gameDisplay):
    print(111111111111111111)
    w, h = pygame.display.get_surface().get_size()
    music_player = music.Music_Player()
    music_player.play_ambtrack2()
    gameDisplay.fill(config.black)
    buttons = [Button("BACK", config.white, pygame.font.Font("assets/fonts/CHILLER.ttf", 70), (90, 60), gameDisplay)]
    gui = pygame.Surface((w, h))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    global paused
                    paused = True
                    print(420420420)
                    utilities.pause()
                #if s button is pressed save the character's stats
                if event.key == pygame.K_s:
                    print('saved the game')
                    utilities.save(player)
                #if l button is pressed load the character's stats
                if event.key == pygame.K_l:
                    utilities.load()
                    player.pos = utilities.loaddata['pos']
                    player.health = utilities.loaddata['health']
                    player.actions = utilities.loaddata['actions']
                    player.items = utilities.loaddata['items']
                    player.hp = utilities.loaddata['hp']
            elif (event.type == pygame.QUIT):
                pygame.quit()
                quit()
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[0].rect.collidepoint(
                    pygame.mouse.get_pos())):
                pass
                # main_menu()


        # for button in buttons:
        #     Button.check_Hover(button, gameDisplay)
        pygame.display.update()
        gui.fill(config.white)

        gameDisplay.blit(gui, (0, 0))
        game_start(player, gameDisplay)
        clock.tick(15)