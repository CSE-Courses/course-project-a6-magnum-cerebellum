import time
import random
import pygame
import math
import music
import config
from health import Bar
from button import Button
from character import Character
from character_UI import char_ui
from character import Character, create_all_characters, random_character
from enemies import Enemy, random_enemy
from player import Player

from os import listdir
from os.path import isfile, join
import map_blit
import transitions

from assets import character_images
from start_game import start_game_play , game_start

import intro_screen
from utilities import save

clock = pygame.time.Clock()
def render_text(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def set_image_location(image, start_x, start_y):
    pos = (start_x, start_y)
    return (image, image.get_rect().move(pos))

def transform_image(image, w, h, n):
    return pygame.transform.scale(image, (int(w / n), int(h / (0.3 * n))))

def get_image_list():
    image_list = []
    character_types = []
    path = 'assets/character_images/'
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    for file in onlyfiles:
        character_types.append(file.split('.')[0])
        image_list.append(pygame.image.load(path + file))
    return image_list, character_types

def get_player_stats(character, size):
    temp_surface = pygame.Surface(size)
    temp_surface.fill((192, 192, 192))
    vertical_offset = 0
    text, rect = render_text("Character : " + character.__str__(), config.CHAR_DETAIL_FONT_LARGE, config.red)
    temp_surface.blit(text, (0, vertical_offset))
    vertical_offset += 50
    text , rect = render_text( "Actions -> " , config.CHAR_DETAIL_FONT_LARGE, config.red)
    temp_surface.blit(text, (0, vertical_offset))
    vertical_offset += 30
    for action in character.actions:
        text , rect = render_text( action.__str__() , config.CHAR_DETAIL_FONT_SMALL, config.red)
        temp_surface.blit(text, (0, vertical_offset))
        vertical_offset += 15
    vertical_offset += 30
    text , rect = render_text( "Items -> " , config.CHAR_DETAIL_FONT_LARGE, config.red)
    temp_surface.blit(text, (0, vertical_offset))
    vertical_offset += 30
    for item in character.items:
        text , rect = render_text( item.__str__() , config.CHAR_DETAIL_FONT_SMALL, config.red)
        temp_surface.blit(text, (0, vertical_offset))
        vertical_offset += 15
    
    return temp_surface

def character_selection(gameDisplay):
    print("selecting characters")
    w, h = pygame.display.get_surface().get_size()
    music_player = music.Music_Player()
    music_player.play_ambtrack2()
    gameDisplay.fill(config.black)
    buttons = [Button("BACK", config.white, pygame.font.Font("assets/fonts/CHILLER.ttf", 70), (90, 60), gameDisplay)]
    character_list = create_all_characters()
    selection_gui = pygame.Surface((w, h))
    image_list, character_types = get_image_list()
    image_rect_list = []
    num_of_images = len(image_list) + 1
    start_x = 0
    start_y = 0
    x_offset = int(w / num_of_images) 
    
    char_detail_surf, char_detail_rect = pygame.Surface((0,0)), pygame.Surface((0,0)) # init to random surface to avoid crash on line 2016
    for elem in image_list:
        transformed_image = transform_image(elem, w, h, num_of_images)
        image_rect_list.append(set_image_location(transformed_image, start_x, start_y))
        start_x += x_offset
    char_detail_offset = start_x
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()
            elif (selection_gui.get_rect().collidepoint(pygame.mouse.get_pos())):
                index = 0
                for char_image, char_rect in image_rect_list:
                    if (char_rect.collidepoint(pygame.mouse.get_pos())):
                        character = Character(character_types[index])
                        size = (x_offset, h)
                        char_detail_surf = get_player_stats(character, size)
                        break
                    index += 1
            #back button when clicked returns to main menu
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[0].rect.collidepoint(
                    pygame.mouse.get_pos())):
                return
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                index = 0
                for char_image, char_rect in image_rect_list:
                    if (char_rect.collidepoint(event.pos)):
                        print("character selected")
                        character = Character(character_types[index])
                        player = Player(character)
                        save(player)

                        game_start(player, gameDisplay)
                    index += 1
            elif (selection_gui.get_rect().collidepoint(pygame.mouse.get_pos())):
                index = 0
                for char_image, char_rect in image_rect_list:
                    if (char_rect.collidepoint(pygame.mouse.get_pos())):
                        character = Character(character_types[index])
                        size = (x_offset, h)
                        char_detail_surf = get_player_stats(character, size)
                        break
                    index += 1

        for button in buttons:
            Button.check_Hover(button, gameDisplay)
        pygame.display.update()
        selection_gui.fill(config.white)
        selection_gui.blit(char_detail_surf, (char_detail_offset, 10))
        for image, image_rect in image_rect_list:
            selection_gui.blit(image, image_rect)
        gameDisplay.blit(selection_gui, (0, 0))
        TextSurf, TextRect = render_text("Choose a Character", config.SPOOKY_BIG_FONT, config.red)
        TextRect.center = ((round(config.display_width / 2)), (round(config.display_height * .9)))
        gameDisplay.blit(TextSurf, TextRect)
        clock.tick(15)    