import pygame
import music
# from davis import gameDisplay, roundup
from important_funcs import funcs, gameDisplay
import config
from button import Button
import math

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
