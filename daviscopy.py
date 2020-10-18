import time
import random
import pygame
import math
import music
import config
from button import Button
import inventory
from inventory import inventoryMain
from important_funcs import funcs
import mainmenu

imp_funcs = funcs

pygame.init()

music_player = music.Music_Player()
music_player.set_volume(1.0)

gameDisplay = pygame.display.set_mode((config.display_width, config.display_height))

pygame.display.set_caption('Davis Hall Escape Simulator 2020')
clock = pygame.time.Clock()


class Checkbox:
    def __init__(self):
        self.draw()

    def draw(self):
        pygame.draw.circle(gameDisplay, config.white, (150, 150), 75)


def reRenderVol(volDisplay, vol, text):
    volDisplay.text = text
    volDisplay.buttonText()
    gameDisplay.fill(config.black)
    volDisplay.createButton(gameDisplay)
    vol.createButton(gameDisplay)


def destroy(self, name_of_class):
    name_of_class.List.remove(self)
    del self

mainmenu.main_menu()

quit()
