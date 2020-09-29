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
from options import option
import mainmenu

imp_funcs = funcs


pygame.init()

music_player = music.Music_Player()
music_player.set_volume(1.0)

gameDisplay = pygame.display.set_mode((config.display_width, config.display_height))


# gameDisplay = pygame.display.set_mode((config.display_width, config.display_height))
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



    # backButton = Button("BACK", config.white, pygame.font.Font("assets/fonts/CHILLER.ttf", 70), (90, 60), gameDisplay)


# def options_menu():
#     music_player = music.Music_Player()
#     music_player.play_normal()
#     w, h = pygame.display.get_surface().get_size()
#
#     gameDisplay.fill(config.black)
#     # buttons = [Button("BACK", white, SPOOKY_SMALL_FONT, (0,0))]
#     current_volume = music_player.get_volume()
#     volumeDisplay = Button(str(funcs.roundup(math.trunc(current_volume * 100))), config.white, config.SPOOKY_SMALL_FONT,
#                            (w / 2, h / 2), gameDisplay)
#     volume = Button("VOLUME", config.white, config.SPOOKY_SMALL_FONT,
#                     (volumeDisplay.pos[0] - 200, volumeDisplay.pos[1]), gameDisplay)
#
#     buttons = [Button("BACK", config.white, pygame.font.Font("assets/fonts/CHILLER.ttf", 70), (90, 60), gameDisplay),
#                Button("<", config.white, config.SPOOKY_SMALL_FONT, (w / 2 - 80, h / 2), gameDisplay),
#                Button(">", config.white, config.SPOOKY_SMALL_FONT, (w / 2 + 80, h / 2), gameDisplay),
#                Button("MUTE", config.white, config.SPOOKY_SMALL_FONT, (w / 2, h / 2 + 100), gameDisplay),
#                Button("1280 x 768", config.white, config.SPOOKY_SMALL_FONT, (w / 2, h / 2 - 200), gameDisplay),
#                Button("1400 x 1050", config.white, config.SPOOKY_SMALL_FONT, (w / 2, h / 2 - 100), gameDisplay)]

        # for button in buttons:
        #     Button.check_Hover(button, gameDisplay)
        #
        # pygame.display.update()
        # clock.tick(15)


mainmenu.main_menu()

quit()
